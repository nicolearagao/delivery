from flask import Flask
from delivery.ext import site
from delivery.ext import config
from delivery.ext import db


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    site.init_app(app)
    db.init_app(app)
    return app



