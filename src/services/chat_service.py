import json

from loguru import logger
from chatkit import hugging_face_client, chat, messages

model = "meta-llama/Meta-Llama-3-8B-Instruct"
client = hugging_face_client.get_client(model)


def ask(question: str) -> str:
    logger.debug(f"{question = }")
    message = chat.call(client, "ask", question=question, model=model)
    logger.debug(f"{message = }")
    answer = message.get("content", "")
    logger.debug(f"{answer = }")
    return answer


def extract(text: str, data_points: dict) -> dict:
    logger.debug(f"{text = } {data_points = }")
    message = chat.call(
        client, "extract", text=text, data_points=data_points, model=model
    )
    logger.debug(f"{message = }")
    data = messages.parse_json_content(message)
    logger.debug(f"{data = }")
    return data


def summarize(text: str) -> str:
    logger.debug(f"{text = }")
    message = chat.call(client, "summarize", text=text, model=model)
    logger.debug(f"{message = }")
    content = message.get("content", "")
    return content


def sentiment(text: str) -> str:
    logger.debug(f"{text = }")
    message = chat.call(client, "sentiment", text=text, model=model)
    logger.debug(f"{message = }")
    content = message.get("content", "")
    logger.debug(f"{content = }")
    return content


def code(language: str, description: str) -> str:
    logger.debug(f"{language = } {description = }")
    message = chat.call(
        client, "code", language=language, description=description, model=model
    )
    logger.debug(f"{message = }")
    content = message.get("content", "")
    logger.debug(f"{content = }")
    return content
