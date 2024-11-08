from datetime import datetime, timedelta
import os

from flask import Blueprint, redirect, render_template, send_from_directory

index_bp = Blueprint("index_bp", __name__)


@index_bp.route("/", methods=["GET"])
def get():
    return render_template("index.html"), 200


# @index_bp.route("/sitemap.xml")
# def sitemap():
#     pages = []
#     lastmod = datetime.now() - timedelta(days=10)
#     for rule in current_app.url_map.iter_rules():
#         if "GET" in rule.methods:
#             exclude_urls = ["/dashboard", "/static"]
#             url = rule.rule
#             page = {"url": url, "lastmod": lastmod.strftime("%Y-%m-%d")}
#             if not any(exclude_url in url for exclude_url in exclude_urls):
#                 pages.append(page)
#     sitemap_xml = render_template("sitemap.xml", pages=pages)
#     return Response(sitemap_xml, mimetype="text/xml")


@index_bp.route("/favicon.ico")
def favicon():
    return send_from_directory(
        os.path.join(index_bp.root_path, "../../static/img/"),
        "favicon.ico",
        mimetype="image/vnd.microsoft.icon",
    )
