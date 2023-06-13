from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timedelta
from jose import jwt

from backend.schemas.users import UserShow, UserCreate
from backend.models.userDAL import UserDal
from backend.models.users import User

from backend import settings


async def create_new_user(user: UserCreate, db_session: AsyncSession) -> UserShow:
    async with db_session.begin():
        user_dal = UserDal(db_session)
        user.hashed_password = get_hashed_password(user.hashed_password)
        new_user = await user_dal.create_user(user)
        return UserShow(id=new_user.id, email=new_user.email, username=new_user.username, is_active=new_user.is_active)


async def login_user(email: str, password: str,  db_session: AsyncSession):
    user = await get_user_by_email(email, db_session)
    if user is None:
        return
    if not verify_password(password, user.hashed_password):
        return
    return user


async def get_user_by_email(email: str, db_session: AsyncSession) -> User:
    async with db_session.begin():
        user_dal = UserDal(db_session)
        return await user_dal.get_user_by_email(email)


def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

