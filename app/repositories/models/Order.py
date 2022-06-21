
from app.repositories.db import db
from datetime import datetime 


order_stock = db.Table('order_stock',
    db.Column('order_id', db.ForeignKey('order.id'), primary_key=True),
    db.Column('stock_id', db.ForeignKey('stock.id'), primary_key=True)
)


class Order(db.Model):

    id = db.Column(db.Integer, primary_key=True)  
    totalAmount = db.Column(db.Float, nullable=True)
    order_date = db.Column(db.Date(), default=datetime.utcnow())
    stock = db.relationship('app.repositories.models.Stock.Stock', secondary=order_stock, back_populates='order')
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship('app.repositories.models.Customer.Customer', back_populates='order')