from flask import Flask

from App.apis import init_blue
from App.ext import init_ext


def create_app():
    app = Flask(__name__)
    init_blue(app=app)
    init_ext(app=app)
    return app