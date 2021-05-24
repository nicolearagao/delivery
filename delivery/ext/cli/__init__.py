from delivery.ext.db import db

def init_app(app):

    @app.cli.command()
    def create_db():
        """Iniciar BD"""
        db.create_all()






