from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer

from backend.schemas.users import UserCreate, UserShow
from backend.auth_app.utils import create_new_user
from backend.database import get_session

auth_router = APIRouter()


@auth_router.post("/auth")
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_session)):
    return await create_new_user(body, db)
