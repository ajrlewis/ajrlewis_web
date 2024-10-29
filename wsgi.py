import os
import sys

from a2wsgi import ASGIMiddleware
from loguru import logger
import uvicorn

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from main import app

logger.debug(f"{app = }")

application = ASGIMiddleware(app, wait_time=5.0)
logger.debug(f"{application = }")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
