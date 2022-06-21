
from cgitb import reset
from tkinter import N
from unittest import result

from flask import jsonify
from app.repositories.db import db
from app.repositories.models.Product import Product
from app.repositories.models.Distributor import Distributor
from app.schemas.ProductSchema import AddProductSchema, ProductSchema
from sqlalchemy.orm import joinedload

class ProductRepository:
    @staticmethod
    def add_product(args):
        new_product = Product(**args)
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def getAllProduct():
        all = Product.query.all()
        return all
        
    @staticmethod
    def get_product_by_name(name):
        product = Product.query.filter_by(name=name).first()
        return product

    @staticmethod
    def get_product_by_id(id):
        product = Product.query.filter_by(id=id).first()
        return product

    @staticmethod
    def delete_product(name):
        product = Product.query.filter_by(name=name).first()
        db.session.delete(product)
        db.session.commit()

    @staticmethod
    def get_id_by_name(name):
        id_obj = Product.query.filter(name==name).first()
        id = id_obj.id
        return id

    @staticmethod
    def get_list_by_name(name):
        # search_format = f"%{name}%"
        lst = Product.query.filter(Product.name.like(name+"%")).all()
        # schema = AddProductSchema(only=["name"], many=True)
        # result = schema.dump(lst)
        return lst

    @staticmethod
    def get_list_of_all_product_names():
        expected = []
        lst = Product.query.all()
        for i in lst:
            name = i.name
            expected.append(name)
        return expected

    @staticmethod
    def get_distributors_join():
        query = db.session.query(Product, Distributor)

        query = query.join(Product, Product.distributor_id == Distributor.id)
        # query = query.options(
        #     joinedload(Product.distributor, innerjoin=True)
        # )
        query = query.all()
        return query