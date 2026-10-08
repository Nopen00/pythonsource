from pydantic import BaseModel
from typing import List

class EventCreate(BaseModel):
    title: str  # 이벤트 제목
    image: str  # 이벤트 이미지
    description: str  # 이벤트 설명
    tags: List[str]  # 그룹화를 위한 이벤트 태그
    location: str  # 이벤트 위치

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "이벤트 제목",
                    "image": "이벤트 이미지 URL 예) https://linktomyimage.com/image.png",
                    "description": "이벤트 설명",
                    "tags": ["python", "fastapi", "book", "launch"],
                    "location": "이벤트 장소",
                }
            ]
        }
    }

class Event(EventCreate):
    id: int  # 자동 생성되는 고유 식별자
