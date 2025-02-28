from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.engine.url import URL

from config import settings
from . import models
from .models import Base


def get_engine(url: URL | str = settings.database_url) -> AsyncEngine:
    return create_async_engine(
        url=url,
        echo=True,
        #         pool_size=2
    )


def get_sessionmaker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


db_url = settings.database_url
engine = get_engine(url=db_url)
sessionmaker = get_sessionmaker(engine)


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


import asyncio

print("drop table")
asyncio.run(drop_table())
print("create table")
asyncio.run(create_table())
