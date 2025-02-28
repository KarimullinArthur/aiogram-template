from sqlalchemy import select

from ..database import sessionmaker
from ..models import User


async def create_user(tg_id) -> None:
    session = sessionmaker()
    user = User(id=tg_id)
    session.add(user)
    await session.commit()


async def get_user(tg_id) -> User | None:
    session = sessionmaker()
    query = select(User).where(User.id == tg_id)
    result = await session.scalar(query)
    return result


async def get_users() -> list[User]:
    session = sessionmaker()
    query = select(User)
    result = await session.scalars(query)
    return list(result)
