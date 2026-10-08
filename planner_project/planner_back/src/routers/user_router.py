from fastapi import APIRouter, HTTPException, status
from models.user import User, UserSignin

user_router = APIRouter(tags=["User"])


users = {}

# 회원가입(회원 생성)
@user_router.post("/signup")
async def post_new_user(data:User):
    if data.email in users:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="사용중인 email 입니다.")

    users[data.email] = data
    return {"message":"User 등록 성공"}


# 로그인 
@user_router.post("/signin")
async def sign_user(data:UserSignin):
    if data.email not in users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="없는 email 입니다.")

    if users[data.email].password != data.password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="비밀번호를 확인해 주세요")

    return {"message":"User 로그인 성공"}