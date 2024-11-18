from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from loguru import logger

from app import token_auth
from schemas.chat_schema import (
    ChatContextMessageSchema,
    ChatRequestSchema,
    ChatResponseSchema,
    ChatAskRequestSchema,
    ChatAskResponseSchema,
    ChatHumanizeRequestSchema,
    ChatHumanizeResponseSchema,
    ChatExtractRequestSchema,
    ChatExtractResponseSchema,
    ChatRequestSchema,
    ChatResponseSchema,
    ChatSentimentResponseSchema,
    ChatCodeRequestSchema,
    ChatCodeResponseSchema,
    ChatKeywordsRequestSchema,
    ChatKeywordsResponseSchema,
)
from services import chat_service


chat_resource = Blueprint(
    "Chat", "chat", url_prefix="/api/chat", description="Chat Operations"
)


@chat_resource.route("/")
class ChatResource(MethodView):
    @chat_resource.arguments(ChatRequestSchema)
    @chat_resource.response(201, ChatContextMessageSchema)
    @token_auth.login_required
    def post(self, data):
        """Chat

        Returns the context message response from a list of context messages.
        """
        context_messages = data.get("context_messages", {})
        logger.debug(f"{context_messages = }")
        context_message = chat_service.completion(context_messages=context_messages)
        return context_message


@chat_resource.route("/humanize")
class ChatAskResource(MethodView):
    @chat_resource.arguments(ChatHumanizeRequestSchema)
    @chat_resource.response(201, ChatHumanizeResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Humanize Text

        Returns the humanized text of input text.
        """
        text = data.get("text", "").encode("UTF-8")
        logger.debug(f"{text = }")
        humanized_text = chat_service.humanize(text=text)
        return {"humanized_text": humanized_text}


@chat_resource.route("/ask")
class ChatAskResource(MethodView):
    @chat_resource.arguments(ChatAskRequestSchema)
    @chat_resource.response(201, ChatAskResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Ask a Question

        Returns the answer to a question supplied in the text.
        """
        question = data.get("question", "").encode("UTF-8")
        logger.debug(f"{question = }")
        answer = chat_service.ask(question=question)
        return {"answer": answer}


@chat_resource.route("/keywords")
class ChatKeywordsResource(MethodView):
    @chat_resource.arguments(ChatKeywordsRequestSchema)
    @chat_resource.response(201, ChatKeywordsResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Keywords

        Returns the keywords from a supplied piece of text.
        """
        text = data.get("text", "").encode("UTF-8")
        logger.debug(f"{text = }")
        keywords = chat_service.keywords(text=text)
        return {"keywords": keywords}


@chat_resource.route("/extract")
class ChatExtractResource(MethodView):
    @chat_resource.arguments(ChatExtractRequestSchema)
    @chat_resource.response(201, ChatExtractResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Extract

        Returns the extract data points from the text supplied.
        """
        text = data.get("text", "").encode("UTF-8")
        data_points = data.get("data_points", {})
        logger.debug(f"{text = } {data_points = }")
        data_points = chat_service.extract(text=text, data_points=data_points)
        return {"data_points": data_points}


@chat_resource.route("/summarize")
class ChatSummarizeResource(MethodView):
    @chat_resource.arguments(ChatRequestSchema)
    @chat_resource.response(201, ChatResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Summarize

        Returns a summary of the text supplied.
        """
        text = data.get("text", "").encode("UTF-8")
        logger.debug(f"{text = }")
        content = chat_service.summarize(text=text)
        return {"content": content}


@chat_resource.route("/sentiment")
class ChatSentimentResource(MethodView):
    @chat_resource.arguments(ChatRequestSchema)
    @chat_resource.response(201, ChatSentimentResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Sentiment

        Returns the sentiment (positive, negative, neutral) of the text supplied.
        """
        text = data.get("text", "").encode("UTF-8")
        logger.debug(f"{text = }")
        sentiment = chat_service.sentiment(text=text)
        return {"sentiment": sentiment}


@chat_resource.route("/code")
class ChatCodeResource(MethodView):
    @chat_resource.arguments(ChatCodeRequestSchema)
    @chat_resource.response(201, ChatCodeResponseSchema)
    @token_auth.login_required
    def post(self, data):
        """Code

        Returns the code in a given language to do a given description.
        """
        language = data.get("language", "").encode("UTF-8")
        description = data.get("description", "").encode("UTF-8")
        logger.debug(f"{language = } {description = }")
        content = chat_service.code(language=language, description=description)
        return {"code": content}
