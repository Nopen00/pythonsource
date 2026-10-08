from fastapi import APIRouter, HTTPException, status
from models.event import Event, EventCreate

event_router = APIRouter(tags=["Events"])

events = []


# 전체 이벤트 조회
# http://127.0.0.1:8000/evnet/ + get
@event_router.get("/", response_model=list[Event])
async def get_events():
    return events

# 특정 이벤트 조회
# http://127.0.0.1:8000/evnet/1 + get
@event_router.get("/{id}", response_model=Event)
async def get_event(id:int):
    for event in events:
        if event.id == id:
            return event
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="이벤트가 없습니다.")

# 이벤트 추가
# http://127.0.0.1:8000/evnet/new + post
@event_router.post("/new", response_model=Event)
async def post_event(data:EventCreate):
    new_id = len(events) + 1
    event = Event(id=new_id, title=data.title, image=data.image, description=data.description, tags=data.tags, location=data.location)
    events.append(event)
    return event

# 특정 이벤트 삭제
# http://127.0.0.1:8000/evnet/1 + delete 
@event_router.delete("/{id}", response_model=list[Event])
async def delete_event(id:int):
    for event in events:
        if event.id == id:
            events.remove(event)
            return events
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="제거할 이벤트가 없습니다.")

# 전체 이벤트 삭제
# http://127.0.0.1:8000/evnet/ + delete
@event_router.delete("/")
async def delete_all_events():
    events.clear()
    return {"message":"모든 Event 삭제 성공"}