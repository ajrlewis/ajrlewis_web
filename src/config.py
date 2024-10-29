import datetime
import os
import secrets

from dotenv import load_dotenv

load_dotenv()


class Config:
    PROJECT_NAME = os.getenv("PROJECT_NAME", "")
    PROJECT_DESCRIPTION = os.getenv("PROJECT_DESCRIPTION", "")
    PROJECT_SUMMARY = os.getenv("PROJECT_SUMMARY", "")
    PROJECT_VERSION = os.getenv("PROJECT_VERSION", "")
    PROJECT_LICENSE = os.getenv("PROJECT_LICENSE", "")
    PROJECT_LICENSE_URL = os.getenv("PROJECT_LICENSE_URL", "")

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

    SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
