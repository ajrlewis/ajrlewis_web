import os
import sys

from a2wsgi import ASGIMiddleware

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from main import app

application = ASGIMiddleware(app)
