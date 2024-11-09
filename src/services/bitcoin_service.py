import datetime
import json
from typing import Optional

import bitcoinkit
from bitcoinkit.vendor import mempool
from loguru import logger


def get_latest_block_data() -> dict:
    block_data = mempool.block.get_latest_block_data()
    return block_data
