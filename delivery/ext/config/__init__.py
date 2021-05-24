def init_app(app):
    app.config['SECRET_KEY'] = "lovecoffee89"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///delivery.db'

