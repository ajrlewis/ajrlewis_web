import io
import json

from aikit.client import hugging_face_client
from aikit.image import image as image_ai
from loguru import logger
import PIL
from werkzeug.datastructures.file_storage import FileStorage

import imagekit


model = "black-forest-labs/FLUX.1-schnell"
client = hugging_face_client.get_client(model=model)


def save_image_to_bytes_io(image: PIL.Image, format: str = "png") -> io.BytesIO:
    image_bytes_io = io.BytesIO()
    image.save(image_bytes_io, format=format)
    image_bytes_io.seek(0)
    return image_bytes_io


def create_image(prompt: str):
    image = image_ai.text_to_image(client, prompt=prompt)
    image_bytes_io = save_image_to_bytes_io(image)
    return image_bytes_io


def read_image(file: FileStorage) -> PIL.Image:
    img = imagekit.load(file.read())
    logger.debug(f"{img = }")
    return img


def extract_text(img: imagekit.Image) -> str:
    text = imagekit.extract_text(img)
    return text
