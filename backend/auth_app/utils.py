from passlib.context import CryptContext

import os
from datetime import datetime, timedelta
from typing import Union, Any
from jose import jwt

from backend.schemas.users import UserShow, UserCreate
from backend.models.userDAL import UserDal


async def create_new_user(user: UserCreate, db_session) -> UserShow:
    async with db_session.begin():
        user_dal = UserDal(db_session)
        user.hashed_password = get_hashed_password(user.hashed_password)
        new_user = await user_dal.create_user(user)
        return UserShow(id=new_user.id, email=new_user.email, username=new_user.username, is_active=new_user.is_active)



SECRET_KEY = "b8dfa5e07d4f5e8b4f96d4872e236406bb3a1aa6b2a18176b945eac3c5254ca0"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
ALGORITHM = "HS256"


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

