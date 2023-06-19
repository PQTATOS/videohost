from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base

from backend.settings import DB_URL


engine = create_async_engine(DB_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


