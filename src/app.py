import os
import sys

from flask import Flask

# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from flask_wtf.csrf import CSRFProtect
from loguru import logger

# csrf = CSRFProtect()
# db = SQLAlchemy()
# migrate = Migrate()


def create_app(Config) -> Flask:
    # template_folder = os.path.abspath(__file__)
    template_folder = "../templates"
    static_folder = "../static"
    logger.debug(f"{template_folder = } {static_folder = }")
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_folder=static_folder,
        template_folder=template_folder,
    )

    logger.debug(f"{app = }")

    app.config.from_object(Config)

    # csrf.init_app(app=app)
    # db.init_app(app=app)
    # migrate.init_app(app=app, db=db)

    with app.app_context():
        from blueprints.index_bp import index_bp

        app.register_blueprint(index_bp, url_prefix="/")

        return app
