import uuid

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import text

from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
    is_active = Column(Boolean, default=False, nullable=False)



