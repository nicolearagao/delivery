from delivery.ext.db import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, nullable=False)
    email = db.Column("email", db.Unicode, unique=True, nullable=False)
    password = db.Column("password", db.Unicode)
    admin = db.Column("admin", db.Boolean)


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column("id", db.Integer, primary_key= True)
    name = db.Column("name", db.Unicode)


class Store(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, unique=True)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    category_id = db.Column("category_id", db.Integer, db.ForeignKey("category.id"))
    user_name = db.Column("user", db.Unicode, db.ForeignKey("user.name"))
    category_name = db.Column("category", db.Unicode, db.ForeignKey("category.name"))
    




