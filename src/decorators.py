from functools import wraps

from flask import request
import imagekit
from loguru import logger

from services import image_service


def load_image(f):
    @wraps(f)
    def _load_image(*args, **kwargs) -> imagekit.Image:
        file = request.files["file"]
        logger.debug(f"{file = } {file.content_type = }")
        allowed_content_types = ("image/png", "image/jpeg", "image/jpg")
        if file.content_type not in allowed_content_types:
            detail = f"Only {allowed_content_types} allowed"
            logger.error(f"{detail = }")
            raise HTTPException(status_code=400, detail=detail)
        img = image_service.read_image(file)
        logger.debug(f"{img = }")
        return f(*args, img=img, **kwargs)

    return _load_image
