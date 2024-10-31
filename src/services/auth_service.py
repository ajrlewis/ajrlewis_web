from loguru import logger

from app import token_auth
from services import user_service


@token_auth.verify_token
def verify_api_key(api_key: str) -> bool:
    if user := user_service.get_user_from_api_key(api_key):
        logger.debug(f"{user = }")
        return True
    logger.error(f"{api_key = } not associated with any user.")
    return False
