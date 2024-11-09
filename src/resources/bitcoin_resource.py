from flask.views import MethodView
from flask_smorest import Blueprint, abort
from loguru import logger

from app import token_auth
from schemas.bitcoin_schema import BitcoinBlockRequestSchema, BitcoinBlockResponseSchema

from services import bitcoin_service

bitcoin_resource = Blueprint(
    "Bitcoin", "bitcoin", url_prefix="/api/bitcoin", description="Bitcoin Operations"
)


@bitcoin_resource.route("/block")
class BitcoinBlockResource(MethodView):
    @bitcoin_resource.response(200, BitcoinBlockResponseSchema())
    def get(self):
        """Get the latest block data."""
        block_data = bitcoin_service.get_latest_block_data()
        return block_data
