from sqlalchemy.orm import Mapped

from .base import *


class WelcomeMassage(Base):
    __tablename__ = "welcome_messages"

    id: Mapped[int_pk]
