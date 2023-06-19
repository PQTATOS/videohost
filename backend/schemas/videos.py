from pydantic import BaseModel
from datetime import datetime


class VideoUpload(BaseModel):
    title: str
    description: str
    filename: str
    user_id: int


class VideoRead(BaseModel):
    title: str
    description: str
    link: str
    user_id: int
    created_at: datetime
    like_count: int


class VideoPreview(BaseModel):
    id: int
    title: str
    link: str
    user_id: int
    published_at: datetime

    class Config:
        orm_mode = True


