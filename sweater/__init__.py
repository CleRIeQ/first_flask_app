import os

from flask import Flask
from flask_migrate import Migrate
from . import models, routes
from sweater.routes import app_route
from .models import db, manager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:zsa21245sd@localhost:5432/flask_test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = db.init_app(app)
manager = manager.init_app(app)
app.secret_key = os.urandom(24)
migrate = Migrate(app, db)
app.register_blueprint(app_route)


