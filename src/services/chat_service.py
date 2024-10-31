from typing import Optional

from loguru import logger
import chatkit


def scrape(url: str) -> dict:
    logger.debug(f"{url = }")
    data = webkit.scrape.text_from_url(url)
    logger.debug(f"{data = }")
    return data
