from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os
import secrets
import hashlib


db = SQLAlchemy()
DB_NAME = "database.db"
secret_key = secrets.token_hex(16)
secret_key_hashed = hashlib.sha256(secret_key.encode()).hexdigest()


def create_app():
    """
    Initializes and configures the Flask application.

    :return: Initialized Flask app instance.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key_hashed
    path = os.path.join(app.root_path, DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path
    db.init_app(app)

    from .home import views
    from .log import auth
    from .share import posts

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(posts, url_prefix="/")

    from .models import User, Post, Comment

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    return app


def create_database(app):
    """
    Creates the database if it does not exist.

    :param app: Flask app instance.
    """
    with app.app_context():
        if not path.exists(app.config['SQLALCHEMY_DATABASE_URI']):
            db.create_all()
