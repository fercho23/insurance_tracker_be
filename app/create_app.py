import logging

from config import Config
from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return app
