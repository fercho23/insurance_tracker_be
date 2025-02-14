# flake8: noqa: E402, F403

import logging

from config import Config

# from flask_cors import CORS
from dotenv import load_dotenv
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

from .models import *
from .routes import *
from .schemas import *
