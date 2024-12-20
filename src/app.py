import os
import sys

from flask import Flask
from flask_httpauth import HTTPTokenAuth
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_smorest import Api
from flask_cors import CORS
from loguru import logger

db = SQLAlchemy()
migrate = Migrate()
token_auth = HTTPTokenAuth(scheme="Bearer")  # 'Authorization: Bearer Your-API-Key'
cors = CORS()


def create_app(Config) -> Flask:
    # Create and configure application and globals
    template_folder = "../templates"
    static_folder = "../static"
    logger.debug(f"{template_folder = } {static_folder = }")
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder=static_folder,
        template_folder=template_folder,
    )
    app.config.from_object(Config)
    logger.debug(f"{app = }")

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)  # after db is configured.
    cors.init_app(app=app, resources={r"*": {"origins": "*"}})

    with app.app_context():
        # Configure authentication service
        from services import auth_service

        # Register blueprints
        from blueprints import index_bp
        from blueprints import api_bp

        app.register_blueprint(index_bp, url_prefix="/")
        app.register_blueprint(api_bp, url_prefix="/api")

        # Register API resources
        api = Api(app)

        from resources import bitcoin_resource
        from resources import chat_resource
        from resources import image_resource
        from resources import web_resource

        api.register_blueprint(bitcoin_resource)
        api.register_blueprint(chat_resource)
        api.register_blueprint(image_resource)
        api.register_blueprint(web_resource)

        return app
