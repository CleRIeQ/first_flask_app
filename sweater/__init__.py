import os

from flask import Flask

from . import models, routes
from sweater.routes import app_route
from .models import db, manager, migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:zsa21245sd@localhost:5432/flask_test"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
manager.init_app(app)
app.secret_key = os.urandom(24)
migrate.init_app(app, db)
app.register_blueprint(app_route)


