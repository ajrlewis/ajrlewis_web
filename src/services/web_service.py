from typing import Optional

from loguru import logger
import webkit


def scrape(url: str) -> dict:
    logger.debug(f"{url = }")
    data = webkit.scrape.data_from_url(url)
    logger.debug(f"{data = }")
    return data


def search(keywords: str, max_results: int) -> list[dict]:
    logger.debug(f"{keywords = } {max_results = }")
    results = webkit.search.duckduckgo_search(
        keywords=keywords, max_results=max_results
    )
    logger.debug(f"{results = }")
    return results
