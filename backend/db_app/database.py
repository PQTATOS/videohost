from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import MetaData, Table, Column, Integer, String

import asyncio

engine = create_async_engine("postgresql+asyncpg://postgres:gQ2mAKBTbW@localhost:5432/videohost_test", echo=True)

metadata = MetaData()

users = Table('user', metadata,
              Column('id', Integer, primary_key=True, index=True),
              Column('email', String(100), index=True),
              Column('username', String(100), index=True),
              Column('hashed_password', String(200)),
              Column('first_name', String(100)),
              Column('last_name', String(100))
              )

