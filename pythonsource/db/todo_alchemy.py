# === Todo 관리 ====
# 1. 추가 2. 목록 3. 완료처리 4. 삭제 5. 종료
# 선택 : 1
# 할 일 내용을 입력하세요: 내용입력...
# 등록되었습니다.
# === Todo 관리 ====
# 1. 추가 2. 목록 3. 완료처리 4. 삭제 5. 종료
# 선택 : 2
# ----------------------------------
# 1. [미완료] 강아지 목욕(2026-08-20 12:38:07)
# === Todo 관리 ====
# 1. 추가 2. 목록 3. 완료처리 4. 삭제 5. 종료
# 선택 : 3
# 완료 처리할 일 번호를 입력하세요: 1
# 완료 처리되었습니다.
# === Todo 관리 ====
# 1. 추가 2. 목록 3. 완료처리 4. 삭제 5. 종료
# 선택 : 4
# 삭제 처리할 일 번호를 입력하세요: 1
# 삭제 처리되었습니다.


# 데이터베이스 테이블 구조
# todo_id 자동증가,pk
# title not null
# is_done number(1) default 0
# created_at 작성일자 sysdate
import os
from datetime import datetime
from typing import Optional

import oracledb
from dotenv import load_dotenv
from sqlalchemy import (
    DateTime,
    Identity,
    Numeric,
    String,
    create_engine,
    select,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
)

load_dotenv()
password = os.getenv("ORACLE_PASSWORD")

# echo=False로 두면 터미널에 불필요한 SQL 로그가 뜨지 않아 메뉴를 보기 편합니다.
engine = create_engine(
    f"oracle+oracledb://python_user:{password}@localhost:1521/?service_name=xe",
    echo=False
)

# 1. 모델(테이블) 정의
class Base(DeclarativeBase):
    pass

class Todo(Base):
    __tablename__ = "todos"

    todo_id: Mapped[int] = mapped_column(
        Numeric(10, 0),
        Identity(start=1, increment=1),
        primary_key=True
    )
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    is_done: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[Optional[datetime]] = mapped_column(DateTime, default=datetime.now)

    def __repr__(self):
        status = '완료' if self.is_done else '미완료'
        created_str = self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else ''
        return f"{self.todo_id}. [{status}] {self.title} ({created_str})"

# 테이블 자동 생성
Base.metadata.create_all(engine)


# 2. 기능 함수 정의
def add_todo():
    '''할 일 추가 (Create)'''
    title = input('할 일 내용을 입력하세요: ').strip()
    if not title:
        print("내용을 입력해주세요.\n")
        return

    with Session(engine) as session:
        todo = Todo(title=title)
        session.add(todo)
        session.commit()
        
    print("등록되었습니다.\n")


def list_todos():
    '''할 일 목록 출력 (Select)'''
    with Session(engine) as session:
        stmt = select(Todo).order_by(Todo.todo_id)
        todos = session.scalars(stmt).all()

        if not todos:
            print('등록된 할 일 목록이 없습니다.\n')
            return

        print('-' * 45)
        for todo in todos:
            status = '완료' if todo.is_done else '미완료'
            created_str = todo.created_at.strftime('%Y-%m-%d %H:%M:%S') if todo.created_at else ''
            print(f"{todo.todo_id}. [{status}] {todo.title} ({created_str})")
        print('-' * 45)
        print()


def update_todo():
    '''완료 처리 (Update)'''
    list_todos()
    input_id = input('완료 처리할 일 번호를 입력하세요: ').strip()
    
    if not input_id.isdigit():
        print("올바른 번호를 입력해주세요.\n")
        return

    with Session(engine) as session:
        todo = session.get(Todo, int(input_id))
        if todo:
            todo.is_done = True
            session.commit()
            print('완료 처리되었습니다.\n')
        else:
            print('해당 번호가 없습니다.\n')


def delete_todo():
    '''할 일 삭제 (Delete)'''
    list_todos()
    input_id = input("삭제 처리할 일 번호를 입력하세요: ").strip()
    
    if not input_id.isdigit():
        print("올바른 번호를 입력해주세요.\n")
        return

    with Session(engine) as session:
        todo = session.get(Todo, int(input_id))
        if todo:
            session.delete(todo)
            session.commit()
            print("삭제 처리되었습니다.\n")
        else:
            print("해당 번호가 없습니다.\n")


def menu():
    while True:
        print("=== Todo 관리 ===")
        print("1. 추가 2. 목록 3. 완료처리 4. 삭제 5. 종료")

        choice = input("선택 : ").strip()

        if choice == "1":
            add_todo()
        elif choice == "2":
            list_todos()
        elif choice == "3":
            update_todo()
        elif choice == "4":
            delete_todo()
        elif choice == "5":
            print("종료합니다.")
            break
        else:
            print("번호를 확인해 주세요.\n")


if __name__ == '__main__':
    menu()