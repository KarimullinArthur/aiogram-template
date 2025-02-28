from sqlalchemy.orm import Mapped

from .base import *


class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[big_int_pk]
    created_at: Mapped[created_at]
