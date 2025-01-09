from typing import Optional

from loguru import logger
import webkit


def scrape(url: str) -> dict:
    logger.debug(f"{url = }")
    data = webkit.scrape.data_from_url(url)
    # logger.debug(f"{data = }")
    return data


def search(query: str, max_results: int) -> list[dict]:
    logger.debug(f"{query = } {max_results = }")
    # results = webkit.search.duckduckgo(
    results = webkit.search.google(query=query, max_results=max_results)
    # logger.debug(f"{results = }")
    return results
