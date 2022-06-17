from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
manager = LoginManager()


class UserModel(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    some = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<User {self.username}>"


class ProfileModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    old = db.Column(db.Integer)
    city = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id))

    def __repr__(self):
        return f"<profiles {self.id}>"


@manager.user_loader
def load_user(user_id):
    return UserModel.query.get(user_id)
