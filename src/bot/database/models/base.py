from typing import Annotated
from datetime import datetime
from datetime import timezone

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import BigInteger
from sqlalchemy.orm import mapped_column


int_pk = Annotated[int, mapped_column(primary_key=True, unique=True, autoincrement=False)]
big_int_pk = Annotated[int, mapped_column(primary_key=True, unique=True, autoincrement=False, type_=BigInteger)]
created_at = Annotated[datetime, mapped_column(default=datetime.now(timezone.utc))]

# For sqliteless db
# created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]


class Base(DeclarativeBase):
    pass
