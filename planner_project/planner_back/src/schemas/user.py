from pydantic import BaseModel
from typing import List,Optional

# 사용자가 생성한 이벤트
class User(BaseModel):
    email: str  
    password: str  
    events: Optional[List[str]]      

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "fastapi@gmail.com",
                    "password": "strong!!!",                  
                    "events": [],                   
                }
            ]
        }
    }

class UserSignin(BaseModel):
    email: str  
    password: str          

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "email": "fastapi@gmail.com",
                    "password": "strong!!!",                
                               
                }
            ]
        }
    }