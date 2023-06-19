from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from backend.schemas.users import UserCreate, UserShow
from backend.utils.utils import create_token, get_hashed_password, verify_password, get_current_user
from backend.database import get_session
from backend.models.DAL import UserDal
from backend.settings import ACCESS_TOKEN_EXPIRE_MINUTES

auth_router = APIRouter(prefix="/auth", tags=["auth"])


@auth_router.post("/signup")
async def create_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    async with session.begin():
        user_dal = UserDal(session)

        check = await user_dal.get_user_by_email(user.email)
        if check is not None:
            raise HTTPException(
                status_code=400, detail="Email already exists!")

        user.hashed_password = get_hashed_password(user.hashed_password)
        new_user = await user_dal.create_user(user)
        access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
        # create jwt token
        access_token = create_token(
            {"sub": str(new_user.id)}, expires_delta=access_token_expires)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }


@auth_router.post("/login")
async def authenticate_user(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_session)):
    async with session.begin():
        user_dal = UserDal(session)
        user = await user_dal.get_user_by_email(form_data.username)
        if user is None:
            raise HTTPException(status_code=400, detail="Email does not exists!")

        if not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect password!")

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        # create jwt token
        access_token = create_token(
            {"sub": str(user.id)}, expires_delta=access_token_expires)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }


@auth_router.get("/me")
async def get_user(user: int = Depends(get_current_user)):
    return user
