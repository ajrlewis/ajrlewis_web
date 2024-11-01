from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from loguru import logger

from app import token_auth
from schemas.chat_schema import (
    ChatAskRequestSchema,
    ChatAskResponseSchema,
    ChatExtractRequestSchema,
    ChatExtractResponseSchema,
    ChatRequestSchema,
    ChatResponseSchema,
    ChatCodeRequestSchema,
    ChatCodeResponseSchema,
)
from services import chat_service


chat_resource = Blueprint(
    "chat", "chat", url_prefix="/api/chat", description="Chat Operations"
)


@chat_resource.route("/ask/")
class ChatAskResource(MethodView):
    @chat_resource.arguments(ChatAskRequestSchema)
    @chat_resource.response(201, ChatAskResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Ask

        Returns the answer to a question supplied in the text.
        """
        logger.debug(f"{data = }")
        question = data.get("question")
        logger.debug(f"{question = }")
        answer = chat_service.ask(question=question)
        return {"answer": answer}


@chat_resource.route("/extract/")
class ChatExtractResource(MethodView):
    @chat_resource.arguments(ChatExtractRequestSchema)
    @chat_resource.response(201, ChatExtractResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Extract

        Returns the extract data points from the text supplied.
        """
        logger.debug(f"{data = }")
        text = data.get("text")
        data_points = data.get("data_points")
        logger.debug(f"{text = } {data_points = }")
        data_points = chat_service.extract(text=text, data_points=data_points)
        return {"data_points": data_points}


@chat_resource.route("/summarize/")
class ChatSummarizeResource(MethodView):
    @chat_resource.arguments(ChatRequestSchema)
    @chat_resource.response(201, ChatResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Summarize

        Returns a summary of the text supplied.
        """
        logger.debug(f"{data = }")
        text = data.get("text")
        logger.debug(f"{text = }")
        content = chat_service.summarize(text=text)
        return {"content": content}


@chat_resource.route("/sentiment/")
class ChatSentimentResource(MethodView):
    @chat_resource.arguments(ChatRequestSchema)
    @chat_resource.response(201, ChatResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Sentiment

        Returns the sentiment (positive, negative, neutral) of the text supplied.
        """
        logger.debug(f"{data = }")
        text = data.get("text")
        logger.debug(f"{text = }")
        content = chat_service.sentiment(text=text)
        return {"content": content}


@chat_resource.route("/code/")
class ChatCodeResource(MethodView):
    @chat_resource.arguments(ChatCodeRequestSchema)
    @chat_resource.response(201, ChatCodeResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Code

        Returns the code in a given language to do a given description.
        """
        logger.debug(f"{data = }")
        language = data.get("language")
        description = data.get("description")
        logger.debug(f"{language = } {description = }")
        content = chat_service.code(language=language, description=description)
        return {"code": content}
