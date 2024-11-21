from flask.views import MethodView
from flask_smorest import Blueprint, abort
from loguru import logger

from app import token_auth
from schemas.bitcoin_schema import (
    BitcoinBlockRequestSchema,
    BitcoinBlockResponseSchema,
    BitcoinPriceRequestSchema,
    BitcoinPriceResponseSchema,
)

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


@bitcoin_resource.route("/price")
class BitcoinPriceResource(MethodView):
    @bitcoin_resource.arguments(BitcoinPriceRequestSchema, location="query")
    @bitcoin_resource.response(200, BitcoinPriceResponseSchema())
    @token_auth.login_required
    def get(self, params: dict):
        """Get the latest bitcoin price data."""
        logger.debug(f"{params = }")
        currency = params.get("currency", "USD").upper()
        logger.debug(f"{currency = }")
        df = bitcoin_service.get_current_price(currency=currency)
        value = 0
        sats_value = 0
        if df is not None:
            logger.debug(f"{df = }")
            value = df.iloc[0][currency]
            logger.debug(f"{value = }")
            sats_value = int(round(100_000_000 / value))
            logger.debug(f"{sats_value = }")
        return {
            "currency": currency,
            "currency_per_bitcoin": value,
            "sats_per_currency": sats_value,
        }
