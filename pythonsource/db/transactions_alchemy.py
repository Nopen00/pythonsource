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
    func,
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

# echo=False로 설정하여 콘솔에 쿼리 로그가 찍히지 않도록 구성
engine = create_engine(
    f"oracle+oracledb://python_user:{password}@localhost:1521/?service_name=xe",
    echo=False
)


# 1. 모델(테이블) 정의
class Base(DeclarativeBase):
    pass


class Transaction(Base):
    __tablename__ = "transactions"

    tx_id: Mapped[int] = mapped_column(
        Numeric(10, 0),
        Identity(start=1, increment=1),
        primary_key=True
    )
    tx_type: Mapped[str] = mapped_column(String(10), nullable=False)
    amount: Mapped[int] = mapped_column(Numeric(12, 0), nullable=False)
    memo: Mapped[str] = mapped_column(String(2000), nullable=False)
    reg_date: Mapped[Optional[datetime]] = mapped_column(DateTime, server_default=func.sysdate())

    def __repr__(self):
        date_str = self.reg_date.strftime("%Y-%m-%d") if self.reg_date else ""
        return f"{self.tx_id}. [{self.tx_type}] {self.amount:,}원 - {self.memo} ({date_str})"


# 테이블 자동 생성
Base.metadata.create_all(engine)


# 2. 가계부 기능 함수
def add_transaction():
    '''내역 추가 (Create)'''
    tx_type = input("구분을 입력하세요 (수입/지출): ").strip()
    amount_input = input("금액을 입력하세요: ").strip()
    memo = input("내역을 입력하세요: ").strip()
    date_input = input("날짜를 입력하세요 (YYYY-MM-DD, 엔터 시 오늘): ").strip()

    if not amount_input.isdigit():
        print("금액은 숫자만 입력해 주세요.\n")
        return

    # 날짜 입력 처리
    if date_input:
        try:
            reg_date = datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("날짜 형식이 올바르지 않습니다. (YYYY-MM-DD)\n")
            return
    else:
        reg_date = datetime.now()

    with Session(engine) as session:
        tx = Transaction(
            tx_type=tx_type,
            amount=int(amount_input),
            memo=memo,
            reg_date=reg_date
        )
        session.add(tx)
        session.commit()

    print("등록되었습니다.\n")


def list_transaction():
    '''전체 조회 (Select - 날짜순 오름차순)'''
    with Session(engine) as session:
        stmt = select(Transaction).order_by(Transaction.reg_date.asc(), Transaction.tx_id.asc())
        transactions = session.scalars(stmt).all()

        if not transactions:
            print("등록된 가계부 목록이 없습니다.\n")
            return

        print("-" * 50)
        for tx in transactions:
            date_str = tx.reg_date.strftime("%Y-%m-%d") if tx.reg_date else ""
            print(f"{tx.tx_id}. [{tx.tx_type}] {tx.amount:,}원 - {tx.memo} ({date_str})")
        print("-" * 50)
        print()


def monthly_transaction():
    '''월별 합계 (Group By 집계)'''
    month = input("조회할 월을 입력하세요 (YYYY-MM): ").strip()

    with Session(engine) as session:
        # 오라클 TO_CHAR 함수를 사용해 년-월 일치 항목 합계 산출
        stmt = (
            select(Transaction.tx_type, func.sum(Transaction.amount))
            .where(func.to_char(Transaction.reg_date, "YYYY-MM") == month)
            .group_by(Transaction.tx_type)
        )
        results = session.execute(stmt).all()

        if not results:
            print(f"{month}월의 가계부 내역이 없습니다.\n")
            return

        print("-" * 50)
        print(f"[{month} 가계부 통계]")
        for tx_type, total_amount in results:
            print(f"{tx_type} : {int(total_amount):,}원")
        print("-" * 50)
        print()


def menu():
    while True:
        print("=== 가계부 ===")
        print("1. 내역 추가 2. 전체 조회 3. 월별 합계 4. 종료")

        choice = input("선택 : ").strip()

        if choice == "1":
            add_transaction()
        elif choice == "2":
            list_transaction()
        elif choice == "3":
            monthly_transaction()
        elif choice == "4":
            print("종료합니다.")
            break
        else:
            print("번호를 확인해 주세요.\n")


if __name__ == "__main__":
    menu()