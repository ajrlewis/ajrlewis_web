import json

from loguru import logger
from chatkit import hugging_face_client, open_ai_client, chat, messages

model = "meta-llama/Meta-Llama-3-8B-Instruct"
client = hugging_face_client.get_client(model)


def extract(text: str, data_points: dict) -> dict:
    logger.debug(f"{text = } {data_points = }")
    message = chat.call(
        client, "extract", text=text, data_points=data_points, model=model
    )
    logger.debug(f"{message = }")
    data = messages.parse_json_content(message)
    logger.debug(f"{data = }")
    return data
