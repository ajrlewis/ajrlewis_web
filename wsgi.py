import os
import sys

from a2wsgi import ASGIMiddleware
from loguru import logger

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from main import app

logger.debug(f"{app = }")

application = ASGIMiddleware(app, wait_time=5.0)
