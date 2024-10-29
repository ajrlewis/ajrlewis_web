import os
import sys

from loguru import logger

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from app import create_app
from config import Config

application = create_app(Config)
logger.debug(f"{application = }")


def main(host: str = "0.0.0.0", port: int = 5000, debug: bool = True):
    logger.debug(f"{host = } {port = } {debug = }")
    application.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    main(*sys.argv[1:])
