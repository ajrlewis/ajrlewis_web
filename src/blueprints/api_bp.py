from flask import Blueprint, render_template

api_bp = Blueprint("api_bp", __name__)


@api_bp.route("/", methods=["GET"])
def get():
    return render_template("api.html"), 200
