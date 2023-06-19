from pydantic import BaseModel
from datetime import datetime


class CommentCreate(BaseModel):
    text: str
    user_id: int
    video_id: int


class CommentView(BaseModel):
    id: int
    text: str
    published_at: datetime
    user_id: int

    class Config:
        orm_mode = True



