from flask import Flask

def create_app():
    app = Flask(__name__)

    from .home import home
    from .log import log
    from .share import share

    return app
