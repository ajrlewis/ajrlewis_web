import json

from aikit.chat import chat, messages
from aikit.client import hugging_face_client
from loguru import logger

model_name = "meta-llama/Meta-Llama-3-8B-Instruct"
client = hugging_face_client.get_client(model_name)


def completion(context_messages: list[dict]) -> dict:
    logger.debug(f"{context_messages = }")
    context_message = chat.completion(
        client, model=model_name, context_messages=context_messages
    )
    logger.debug(f"{context_message = }")
    return context_message


def ask(question: str) -> str:
    logger.debug(f"{question = }")
    model = {
        "name": model_name,
        "system": "You answer questions.",
        "kwargs": {"temperature": 0.3},
    }
    template = {"name": "ask", "kwargs": {"question": question}}
    assistant_message = chat.call(client, model=model, template=template)
    logger.debug(assistant_message)
    answer = assistant_message.get("content", "")
    logger.debug(f"{answer = }")
    return answer


def humanize(text: str) -> str:
    logger.debug(f"{text = }")
    model = {
        "name": model_name,
        "system": "You rewrite text to make it sound more imperfect/human.",
        "kwargs": {"temperature": 0.3},
    }
    template = {"name": "humanize", "kwargs": {"text": text}}
    assistant_message = chat.call(client, model=model, template=template)
    logger.debug(assistant_message)
    humanized_text = assistant_message.get("content", "")
    logger.debug(f"{humanized_text = }")
    return humanized_text


def keywords(text: str) -> str:
    logger.debug(f"{text = }")
    model = {
        "name": model_name,
        "system": "You extract prominent keywords from text.",
        "kwargs": {"temperature": 0.3},
    }
    template = {"name": "keywords", "kwargs": {"text": text}}
    assistant_message = chat.call(client, model=model, template=template)
    logger.debug(assistant_message)
    keywords = assistant_message.get("content", "")
    logger.debug(f"{keywords = }")
    return keywords


def extract(text: str, data_points: dict) -> dict:
    logger.debug(f"{text = } {data_points = }")
    model = {
        "name": model_name,
        "system": "You extract JSON objects from text.",
        "kwargs": {"temperature": 0.3},
    }
    template = {
        "name": "extract",
        "kwargs": {"text": text, "data_points": data_points},
        "parse_json": True,
    }
    assistant_message = chat.call(client, model=model, template=template)
    logger.debug(assistant_message)
    data = assistant_message.get("content", {})
    logger.debug(f"{data = }")
    return data


def summarize(text: str) -> str:
    logger.debug(f"{text = }")
    model = {
        "name": model_name,
        "system": "You summarize text.",
        "kwargs": {"temperature": 0.3},
    }
    template = {"name": "summarize", "kwargs": {"text": text}}
    assistant_message = chat.call(client, model=model, template=template)
    logger.debug(assistant_message)
    summarized_text = assistant_message.get("content", "")
    logger.debug(f"{summarized_text = }")
    return summarized_text


def sentiment(text: str) -> str:
    logger.debug(f"{text = }")
    model = {
        "name": model_name,
        "system": "You compute the sentiment of text.",
        "kwargs": {"temperature": 0.3},
    }
    template = {"name": "sentiment", "kwargs": {"text": text}}
    assistant_message = chat.call(client, model=model, template=template)
    logger.debug(assistant_message)
    text_sentiment = assistant_message.get("content", "")
    logger.debug(f"{text_sentiment = }")
    return text_sentiment


def code(language: str, description: str) -> str:
    logger.debug(f"{language = } {description = }")
    model = {
        "name": model_name,
        "system": "You create code in a given language.",
        "kwargs": {"temperature": 0.3},
    }
    template = {
        "name": "code",
        "kwargs": {"language": language, "description": description},
    }
    assistant_message = chat.call(client, model=model, template=template)
    logger.debug(assistant_message)
    code = assistant_message.get("content", "")
    logger.debug(f"{code = }")
    return code
