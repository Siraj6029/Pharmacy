from app.repositories.db import db




class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50))
    order = db.relationship('app.repositories.models.Order.Order', back_populates='customer')