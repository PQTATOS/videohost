from backend.schemas.users import UserCreate
from backend.models.users import User

from sqlalchemy.ext.asyncio import AsyncSession


class UserDal:
    def __init__(self, db_session: AsyncSession):
        self.session = db_session

    async def create_user(self, body: UserCreate):
        new_user = User(email=body.email, username=body.username, hashed_password=body.hashed_password)
        self.session.add(new_user)
        await self.session.flush()
        return new_user
