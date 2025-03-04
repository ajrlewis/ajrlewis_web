import secrets
from typing import Optional

from loguru import logger

from app import db
from models.user import User


def get_user_from_api_key(api_key: str) -> Optional[User]:
    user = db.session.query(User).filter_by(api_key=api_key).first()
    logger.debug(f"{user = }")
    return user


def create_api_key() -> str:
    api_key = "sk_" + secrets.token_urlsafe(32)
    return api_key
