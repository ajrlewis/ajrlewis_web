from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from loguru import logger

from app import token_auth
from schemas.chat_schema import ChatExtractRequestSchema, ChatExtractResponseSchema
from services import chat_service


chat_resource = Blueprint(
    "chat", "chat", url_prefix="/api/chat", description="Chat Operations"
)


@chat_resource.route("/extract/")
class ChatExtractResource(MethodView):
    @chat_resource.arguments(ChatExtractRequestSchema)
    @chat_resource.response(201, ChatExtractResponseSchema)
    @token_auth.login_required
    def post(self, data):
        logger.debug(f"{data = }")
        text = data.get("text")
        data_points = data.get("data_points")
        logger.debug(f"{text = } {data_points = }")
        data_points = chat_service.extract(text=text, data_points=data_points)
        return {"data_points": data_points}
