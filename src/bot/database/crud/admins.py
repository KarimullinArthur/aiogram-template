from sqlalchemy import select

from ..database import sessionmaker
from ..models import Admin


async def create_admin(tg_id) -> None:
    session = sessionmaker()
    admin = Admin(id=tg_id)
    session.add(admin)
    await session.commit()


async def get_admin(tg_id) -> Admin | None:
    session = sessionmaker()
    query = select(Admin).where(Admin.id == tg_id)
    result = await session.scalar(query)
    return result


async def get_admins() -> list[Admin]:
    session = sessionmaker()
    query = select(Admin)
    result = list(await session.scalars(query))
    return result


async def get_admins_tg_ids() -> list[int]:
    session = sessionmaker()
    query = select(Admin)
    admins = list(await session.scalars(query))
    result = list(map(lambda x: x.id, admins))
    return result



import asyncio
asyncio.run(create_admin(441894644))
# asyncio.run(create_admin(441894645))
# asyncio.run(create_admin(441894646))
# print("GETGETGET")
# a = asyncio.run(get_admins())
# print(a)
# print()
# for x in a:
#     print(x.id)
# print()
# print()
