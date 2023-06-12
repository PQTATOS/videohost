from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData


engine = create_async_engine("postgresql+asyncpg://postgres:gQ2mAKBTbW@localhost:5432/videohost_test", echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


