from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm

from backend.schemas.users import UserCreate, UserShow
from backend.auth_app.utils import create_new_user, login_user, create_token
from backend.database import get_session

auth_router = APIRouter()


@auth_router.post("/signup")
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_session)):
    return await create_new_user(body, db)


@auth_router.post("/login")
async def authenticate_user(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    user = await login_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect data")

    access_token = create_token({"sub": user.email})

    return {"access_token" : access_token, "token_type": "bearer"}
