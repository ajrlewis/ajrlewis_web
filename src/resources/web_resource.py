from flask.views import MethodView
from flask_smorest import Blueprint, abort
from loguru import logger

from app import token_auth
from schemas.web_schema import (
    WebScrapeQueryArgsSchema,
    WebScrapeResponseSchema,
    WebSearchQueryArgsSchema,
    WebSearchResponseSchema,
)

from services import web_service

web_resource = Blueprint(
    "Web", __name__, url_prefix="/api/web", description="Web Operations"
)


@web_resource.route("/scrape")
class WebScrapeResource(MethodView):
    @web_resource.arguments(WebScrapeQueryArgsSchema, location="query")
    @web_resource.response(200, WebScrapeResponseSchema(many=False))
    @token_auth.login_required
    def get(self, params: dict):
        """Scrape a URL for data.

        Extracts useful data from a website given its URL.
        """
        logger.debug(f"{params = }")
        url = params.get("url")
        logger.debug(f"{url = }")
        return web_service.scrape(url=url)


# @web_resource.route("/image_search")
# @web_resource.route("/text_search")
@web_resource.route("/search")
class WebSearchResource(MethodView):
    @web_resource.arguments(WebSearchQueryArgsSchema, location="query")
    @web_resource.response(200, WebSearchResponseSchema(many=False))
    @token_auth.login_required
    def get(self, params: dict):
        """Search the internet.

        Returns web pages relevant to a supplied query.
        """
        logger.debug(f"{params = }")
        query = params.get("query")
        max_results = params.get("max_results", 10)
        logger.debug(f"{query = } {max_results = }")
        results = web_service.search(query=query, max_results=max_results)
        # logger.debug(f"{results = }")
        return {"results": results}
