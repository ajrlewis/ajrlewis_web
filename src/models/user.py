from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app import db


class User(db.Model):
    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    password_hash: Mapped[str] = mapped_column()
    api_key: Mapped[str] = mapped_column()
    is_admin: Mapped[bool] = mapped_column(default=False)
