from app.repositories.db import db
from datetime import datetime
from app.repositories.models.Order import order_stock




class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_entry_date = db.Column(db.Date, default=datetime.utcnow)
    price = db.Column(db.Float, nullable=False)
    expiry = db.Column(db.Date, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('app.repositories.models.Product.Product', back_populates='stock')
    order = db.relationship('app.repositories.models.Order.Order', secondary= order_stock, back_populates='stock')