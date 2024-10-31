from flask.views import MethodView
from flask_smorest import Blueprint, abort
from loguru import logger

from app import token_auth
from schemas.chat_schema import ChatExtractSchema

from services import chat_service


chat_resource = Blueprint(
    "chat", "chat", url_prefix="/api/chat", description="Chat Operations"
)


@chat_resource.route("/extract")
class ChatExtractResource(MethodView):
    # @chat_resource.arguments(WebScrapeQueryArgsSchema, location="query")
    # @chat_resource.response(200, ChatExtractSchema(many=False))
    @chat_resource.arguments(ChatExtractSchema)
    @chat_resource.response(201, dict)
    @token_auth.login_required
    def post(self, data: dict) -> dict:
        """."""
        data = chat_service.extract(data)
        return data
