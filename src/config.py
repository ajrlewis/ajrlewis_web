import datetime
import os
import secrets

from dotenv import load_dotenv

load_dotenv()


class Config:
    API_TITLE = os.getenv("API_TITLE")
    API_VERSION = os.getenv("API_VERSION")
    API_SPEC_OPTIONS = {
        "info": {
            "description": os.getenv("API_SPEC_OPTIONS_DESCRIPTION"),
            "termsOfService": os.getenv("API_SPEC_OPTIONS_TERMS_OF_SERVICE"),
            "contact": os.getenv("API_SPEC_OPTIONS_CONTACT"),
            "license": {
                "name": "MIT License",
                "url": "https://opensource.org/license/mit",
            },
        },
        "security": [{"bearerAuth": []}],
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                }
            }
        },
    }

    OPENAPI_VERSION = "3.0.2"
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_URL_PREFIX = "/"
    OPENAPI_REDOC_PATH = "/api/redoc"
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    OPENAPI_SWAGGER_UI_PATH = "/api/docs"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    OPENAPI_RAPIDOC_PATH = "/api/rapidoc"
    OPENAPI_RAPIDOC_URL = "https://unpkg.com/rapidoc/dist/rapidoc-min.js"

    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    JSON_SORT_KEYS = False

    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER_NAME = os.getenv("MAIL_DEFAULT_SENDER_NAME")
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    REMEMBER_COOKIE_DURATION = datetime.timedelta(
        seconds=int(os.getenv("REMEMBER_COOKIE_DURATION", 600))
    )
    PERMANENT_SESSION_LIFETIME = REMEMBER_COOKIE_DURATION

    SECRET_KEY = secrets.token_urlsafe(32)
