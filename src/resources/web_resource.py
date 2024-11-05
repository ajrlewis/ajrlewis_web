from flask.views import MethodView
from flask_smorest import Blueprint, abort
from loguru import logger

from app import token_auth
from schemas.web_schema import (
    WebScrapeSchema,
    WebScrapeQueryArgsSchema,
    WebSearchSchema,
    WebSearchQueryArgsSchema,
)

from services import web_service

web_resource = Blueprint(
    "Web", "web", url_prefix="/api/web", description="Web Operations"
)


@web_resource.route("/scrape")
class WebScrapeResource(MethodView):
    @web_resource.arguments(WebScrapeQueryArgsSchema, location="query")
    @web_resource.response(200, WebScrapeSchema(many=False))
    @token_auth.login_required
    def get(self, params: dict):
        """Scrape a URL for text"""
        logger.debug(f"{params = }")
        url = params.get("url")
        logger.debug(f"{url = }")
        return web_service.scrape(url=url)


@web_resource.route("/search")
class WebSearchResource(MethodView):
    @web_resource.arguments(WebSearchQueryArgsSchema, location="query")
    # @web_resource.response(200, WebSearchSchema(many=False))
    @token_auth.login_required
    def get(self, params: dict) -> list[dict]:
        """Search the internet for keywords."""
        logger.debug(f"{params = }")
        keywords = params.get("keywords")
        max_results = params.get("max_results")
        logger.debug(f"{keywords = } {max_results = }")
        results = web_service.search(keywords=keywords, max_results=max_results)
        logger.debug(f"{results = }")
        return results
