from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"

    from .home import views
    from .log import auth
    from .share import posts

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(posts, url_prefix="/")

    return app
