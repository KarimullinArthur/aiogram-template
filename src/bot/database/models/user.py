from sqlalchemy.orm import Mapped

from .base import *


class User(Base):
    __tablename__ = "users"

    id: Mapped[big_int_pk]

    created_at: Mapped[created_at]
