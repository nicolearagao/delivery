from flask_sqlachemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
