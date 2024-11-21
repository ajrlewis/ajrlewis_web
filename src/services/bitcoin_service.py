import datetime
import json
from typing import Optional

import bitcoinkit
from bitcoinkit.vendor import mempool
from loguru import logger


def get_latest_block_data() -> dict:
    block_data = mempool.block.get_latest_block_data()
    return block_data


def get_current_price(currency: Optional[str] = None) -> float:
    price = mempool.price.current(currency=currency)
    return price
