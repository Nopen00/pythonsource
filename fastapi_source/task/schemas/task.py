
from pydantic import BaseModel

class TaskCreate(BaseModel):    
    text:str
    done:bool
class TaskUpdate(BaseModel):    
    text:str | None = None
    done:bool | None = None

class TaskRespense(TaskCreate):
    id:int

class TaskPageRespense(BaseModel):
    items:list[TaskRespense]
    total: int
    total_pages: int
    page: int
    size: int



