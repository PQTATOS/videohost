from sqlalchemy import Column, Integer, ForeignKey

from backend.database import Base


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    video_id = Column(Integer, ForeignKey("videos.id"), index=True, nullable=False)