from flask import Flask, render_template

from .auth import auth


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(auth, url_prefix='/')

    return app
