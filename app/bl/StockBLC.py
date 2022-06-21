from app.repositories.ProductRepository import ProductRepository
from app.repositories.db import db
from app.repositories.StockRepository import StockRepository
from app.repositories.models import Stock, Product

class StockBLC:
    @staticmethod
    def add_extra_info(list_of_dict, product_name):
        result = {}
        result["stock"] = list_of_dict
        result["product name"] = product_name["name"]
        total_quantity = 0
        for items in list_of_dict:
            total_quantity = total_quantity + items["quantity"]
        result["total quantity"] = total_quantity
        return result