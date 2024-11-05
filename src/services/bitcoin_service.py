import datetime
import json
from typing import Optional

import bitcoinkit
from loguru import logger


def get_block(timestamp: Optional[str] = None) -> dict:
    if not timestamp:
        timestamp = datetime.datetime.utcnow()
        timestamp = f"{timestamp}"
    logger.debug(f"{timestamp = }")
    # Get block time
    # Get block height
    block_height = 1
    return {"height": block_height}
