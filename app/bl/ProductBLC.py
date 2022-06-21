from itertools import product
from unittest import result
from flask import session
from app.repositories.db import db
from app.repositories.DistributorRepository import DistributorRepository
from app.repositories.ProductRepository import ProductRepository
from app.schemas.ProductSchema import ProductSchema

class Productblc():
    @staticmethod
    def retreive_product(args):
        product = ProductRepository.get_product_by_name(**args)
        schema = ProductSchema()
        result = schema.dump(product)
        return result

    @staticmethod
    def update_product(args):
        product_obj = ProductRepository.get_product_by_id(args["id"])

        if not product_obj:
            return None

        if product_obj.name != args["name"]:
            product_obj = args["name"]
        product_obj.company = args["company"]
        product_obj.formula = args["formula"]
        product_obj.miniQuantity = args["formula"]
        product_obj.distributor_id = args["distributor_id"]
        db.session.commit()

    @staticmethod
    def modify_name_of_list(args):
        modified_list = []
        for item in args:
            modified_list.append(item["name"])
        return modified_list

    @staticmethod
    def get_distributors_join():
        result = ProductRepository.get_distributors_join()
        

        result_list = []
        for item in result:
            item_dict = {
                "product": item[0],
                "distributor": item[1],
            }

            result_list.append(item_dict)
        
        return result_list