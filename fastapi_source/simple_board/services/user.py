from sqlalchemy.orm import Session
from schemas.user import (
    UserCreate,
    UserResponse,
    UserLogin,
    NameChage,
    PasswordChange,
    EmailChage,
)
from repository.models.user import User
from sqlalchemy import select
from exceptions.user import (
    UserAlreadyExistsException,
    UserNotFoundException,
    InvalidePasswordException,
    SamePasswordException
)
from core.security import hash_password, verify_password
from utils.security import create_access_token
from schemas.user import Token

DUMMY_HASH = hash_password('dummypassword')



# CRUD 작업


# 이름 변경
def update_name(db: Session, data: NameChage, user_id: int):
    # 수정할 대상 찾기
    user = db.get(User, user_id)

    if user is None:
        raise UserNotFoundException

    # 수정하기
    user.name = data.name
    db.commit()
    db.refresh(user)
    return user


# 이메일 변경
def update_email(db: Session, data: EmailChage, user_id: int):
    # 수정할 대상 찾기
    user = db.get(User, user_id)

    if user is None:
        raise UserNotFoundException

    # 수정하기
    user.email = data.email
    db.commit()
    db.refresh(user)
    return user


# 비밀번호 변경
def update_password(db: Session, data: PasswordChange, user_id: int):
    # 수정할 대상 찾기
    user = db.get(User, user_id)

    if user is None:
        raise UserNotFoundException

    # current_password가 데이터 베이스 비밀번호와 동일한가?
    if not verify_password(data.current_password, user.password):
        raise InvalidePasswordException

    # new_password 데이터 베이스 비밀번호와 동일한가?
    if verify_password(data.new_password, user.password):
        raise SamePasswordException

    # 수정하기 - new_password 암호화 후 업데이트

    user.password = hash_password(data.new_password)
    db.commit()
    db.refresh(user)
    return user


# 로그인
def authenticate(db: Session, data: UserLogin):

    user = db.scalar(select(User).where(User.email == data.email))

    # 회원가입 정보가 없는경우
    if user is None:
        # timing attack 방지
        verify_password(data.password, DUMMY_HASH)
        raise UserNotFoundException

    # 비밀번호 검증 틀린 경우
    if not verify_password(data.password, user.password):
        raise InvalidePasswordException

    access_token = create_access_token(data={'sub':str(user.user_id)})

    return Token(access_token=access_token)


# 회원가입
# 비밀번호 => 암호화
def register(db: Session, data: UserCreate):
    # 동일한 이메일로 가입된 정보가 있는가?
    # select * from board_users where email = '가입하려고 하는 이메일'
    existing_user = db.scalar(select(User).where(User.email == data.email))

    if existing_user:
        raise UserAlreadyExistsException

    # 가입된 정보가 없을때 회원가입
    user = User(email=data.email, password=hash_password(data.password), name=data.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
