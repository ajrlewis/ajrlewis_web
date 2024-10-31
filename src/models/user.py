from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app import db


class User(db.Model):
    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(16), unique=True)
    password_hash: Mapped[str] = mapped_column(db.String(102), nullable=True)
    api_key: Mapped[str] = mapped_column(
        db.String(46)
    )  # "sk_" + secrets.token_urlsafe(32)
    is_admin: Mapped[bool] = mapped_column(default=False)
