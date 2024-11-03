import io
from io import BytesIO
from PIL import Image
from flask import Response, send_file

import base64

from flask.views import MethodView
from flask_smorest import Blueprint, abort
import imagekit
from loguru import logger

from app import token_auth
from schemas.image_schema import (
    ImageRequestSchema,
    ImageResponseSchema,
    ImageCreateRequestSchema,
    ImageTextExtractResponseSchema,
)
from services import image_service
from decorators import load_image

image_resource = Blueprint(
    "Image", "image", url_prefix="/api/image", description="Image Operations"
)


@image_resource.route("/create")
class ImageCreateResource(MethodView):
    @image_resource.arguments(ImageCreateRequestSchema)
    # @token_auth.login_required
    # @load_image
    def post(self, data: dict):
        """Create an image from text.

        Creates and returns an image from a text prompt.
        """
        prompt = data.get("prompt", "")
        logger.debug(f"{prompt = }")
        image = image_service.create_image(prompt=prompt)
        filename = "test.png"
        content_type = "png"
        return send_file(
            image,
            download_name=filename,
            as_attachment=True,
            mimetype=content_type,
        )


@image_resource.route("/extract/")
class ImageTextExtractResource(MethodView):
    @image_resource.arguments(ImageRequestSchema, location="files")
    # @image_resource.response(201, ImageTextExtractResponseSchema)
    # @token_auth.login_required
    @load_image
    def post(self, data: dict, img: imagekit.Image):
        """Text Extract

        Extracts text from an image.
        """
        logger.debug(f"{img = }")
        text = image_service.extract_text(img)
        return {"text": text}
