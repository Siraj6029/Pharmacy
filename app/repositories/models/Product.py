from app.repositories.db import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    company = db.Column(db.String(50), nullable=False)
    formula = db.Column(db.String(50))
    minQuantity = db.Column(db.Integer)
    distributor_id = db.Column(db.Integer, db.ForeignKey('distributor.id'))
    distributor = db.relationship('app.repositories.models.Distributor.Distributor', back_populates='products')
    stock = db.relationship('app.repositories.models.Stock.Stock', back_populates='product')
