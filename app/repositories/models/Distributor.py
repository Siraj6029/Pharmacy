from enum import unique
from app.repositories.db import db

class Distributor(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(50))
    contact = db.Column(db.String(50))
    products = db.relationship('app.repositories.models.Product.Product', back_populates='distributor')