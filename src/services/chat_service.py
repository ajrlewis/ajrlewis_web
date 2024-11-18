import json

from aikit.chat import chat, messages
from aikit.client import hugging_face_client
from loguru import logger

model = "meta-llama/Meta-Llama-3-8B-Instruct"
client = hugging_face_client.get_client(model)


def completion(context_messages: list[dict]) -> dict:
    logger.debug(f"{context_messages = }")
    context_message = chat.completion(client, context_messages=context_messages)
    logger.debug(f"{context_message = }")
    # max_tokens
    # temperature
    # top_p
    # frequency_penalty
    # presence_penalty
    return context_message


def ask(question: str) -> str:
    logger.debug(f"{question = }")
    message = chat.call(client, "ask", question=question, model=model)
    logger.debug(f"{message = }")
    answer = message.get("content", "")
    logger.debug(f"{answer = }")
    return answer


def humanize(text: str) -> str:
    logger.debug(f"{text = }")
    message = chat.call(client, "humanize", text=text, model=model)
    logger.debug(f"{message = }")
    humanized_text = message.get("content", "")
    logger.debug(f"{humanized_text = }")
    return humanized_text


def keywords(text: str) -> str:
    logger.debug(f"{text = }")
    system_content = "You are an expert text analyst."
    message = chat.call(
        client, "keywords", system_content=system_content, text=text, model=model
    )
    logger.debug(f"{message = }")
    keywords = message.get("content", "")
    logger.debug(f"{keywords = }")
    return keywords


def extract(text: str, data_points: dict) -> dict:
    logger.debug(f"{text = } {data_points = }")
    assistant_message = chat.call(
        client,
        "extract",
        system_content="You extract JSON objects from text.",
        text=text,
        data_points=data_points,
        model=model,
    )
    print(assistant_message, type(assistant_message))
    data = messages.parse_json_content(assistant_message)
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
