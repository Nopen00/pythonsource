# 타입 점검
from pydantic import BaseModel

class CommentCreate(BaseModel):
    body:str
    user_id:int
    board_id:int


class CommentUpdate(BaseModel):
    body:str | None = None




