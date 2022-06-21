from app.repositories.db import db
from app.repositories.models import Stock

class StockRepository:
    @staticmethod
    def get_session():
        return db.session

    @staticmethod
    def add_stock(stock):
        new_stock = Stock(**stock)
        db.session.add(new_stock)
        db.session.commit()
        return new_stock

    @staticmethod
    def all_stocks():
        all_stocks = Stock.query.all()
        return all_stocks

    @staticmethod
    def get_stock_by_product_id(id):
        
        stock = Stock.query.filter(Stock.product_id==id).filter(Stock.quantity>0).all()
        
        return stock
    