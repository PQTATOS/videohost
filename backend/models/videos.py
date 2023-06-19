from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

from backend.database import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(String)
    link = Column(String, nullable=False)
    like_count = Column(Integer, default=0)
    published_at = Column(DateTime, default=datetime.utcnow())
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)


