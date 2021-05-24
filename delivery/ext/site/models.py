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
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode)


class Store(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, unique=True)
    image = db.Column("image", db.Unicode)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    category_id = db.Column("category_id", db.Integer, db.ForeignKey("category.id"))

    user_name = db.relationship("User", foreign_keys=user_id)
    category = db.relationship("Category", foreign_keys=category_id)


class Items(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.Unicode, unique=True)
    image = db.Column("image", db.Unicode)
    price = db.Column("price", db.Numeric)
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("store.id"))
    available = db.Column("available", db.Boolean)

    store = db.relationship("Store", foreign_key=store_id)


class Address(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    zip = db.Column("zipcode", db.Unicode)
    address = db.Column("address", db.Unicode)
    user_id = db.Column("user_id", db.Unicode, db.ForeignKey("user.id"))

    user = db.relationship("User", foreign_key=user_id)


class Order(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    user_id = db.Column("user_id", db.Integer, db.ForeignKey("user.id"))
    store_id = db.Column("store_id", db.Integer, db.ForeignKey("store.id"))
    address_id = db.Column("address-id", db.Integer, db.ForeignKey("address.id"))

    user = db.relationship("User", foreign_key=user_id)
    store = db.relationship("Store", foreign_key=store_id)
    address = db.relationship("Address", foreign_key=address_id)


class OrderItems(db.Model):
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))
    items_id = db.Column("items_id", db.Integer, db.ForeignKey("items.id"))
    quantity = db.Column("quantity", db.Integer)
    id = db.Column("id", db.Integer, primary_key=True)

    order = db.relationship("Order", foreign_key=order_id)
    items = db.relationship("Items", foreign_key=items_id)


class Checkout(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    payment = db.Column("payment", db.Unicode)
    total = db.Column("Total", db.Numeric)
    created_at = db.Column("created_at", db.DateTime)
    completed = db.Column("completed", db.Boolean)
    order_id = db.Column("order_id", db.Integer, db.ForeignKey("order.id"))

    order = db.relationship("Order", foreign_key=order_id)


