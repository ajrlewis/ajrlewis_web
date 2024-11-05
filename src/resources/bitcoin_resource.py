from flask.views import MethodView
from flask_smorest import Blueprint, abort
from loguru import logger

from app import token_auth
from schemas.bitcoin_schema import BitcoinBlockRequestSchema

from services import bitcoin_service

bitcoin_resource = Blueprint(
    "Bitcoin", "bitcoin", url_prefix="/api/bitcoin", description="Bitcoin Operations"
)


@bitcoin_resource.route("/block")
class BitcoinBlockResource(MethodView):
    @bitcoin_resource.arguments(BitcoinBlockRequestSchema, location="query")
    # @bitcoin_resource.response(200, WebScrapeSchema(many=False))
    # @token_auth.login_required
    def get(self, params: dict):
        """Scrape a URL for text"""
        timestamp = params.get("timestamp")
        block_stats = bitcoinkit.get_block_stats(timestamp=timestamp)
        return block_stats
