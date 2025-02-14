# flake8: noqa: E402, F403

import logging

from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .create_app import create_app

app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
logger = logging.getLogger(__name__)

from .models import *
from .routes import *
from .schemas import *
