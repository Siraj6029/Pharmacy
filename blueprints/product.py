
from unittest import result
from flask import Blueprint, jsonify
from app.repositories.ProductRepository import ProductRepository
from webargs import fields
from webargs.flaskparser import use_args
from app.schemas.ProductSchema import AddProductSchema, ProductSchema, UpdateProductSchema, ProductDistributorsSchema
from http import HTTPStatus
from app.bl.ProductBLC import Productblc
from app.repositories.db import db
from difflib import get_close_matches

bp = Blueprint('product', __name__)


@bp.route('/product/add', methods=['POST'])
@use_args(AddProductSchema, location="json")
def addProduct(args:dict):

    """
    This method is used for adding new product

    :param : name of product
    :param : company of product
    :param : formula of product
    :param : minimum quantity
    :param : distributor id 
    return Dict
    """

    try:
        
        product_cteated = ProductRepository.add_product(args)
        schema = ProductSchema(many=False)
        result = schema.dump(product_cteated)
        return jsonify(result), HTTPStatus.OK    #needs to ask that why not dumping
    except Exception as e:
        print(e)
        return jsonify({"Error": e.args[0]}), HTTPStatus.UNPROCESSABLE_ENTITY
        

@bp.route("/product/all", methods=["GET"])
def get_all_product():
    """
    This method is used to get all products

    :param : it has no parameter to pass

    return Object
    """
    try:
        all_products = ProductRepository.getAllProduct()
        schema = ProductSchema(many=True)
        result = schema.dump(all_products)
        return jsonify(result)
    except Exception as e:
        print(e)
        return jsonify({"error": e.args[0]}), HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/product/retrieve", methods=["GET"])
@use_args({"name": fields.Str(required=True)}, location="query")
def get_product(args):
    try:
        product = Productblc.retreive_product(args)
        return jsonify(product)
    except Exception as e:
        print(e)
        return jsonify({"error": e.args[0]}), HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route('/product/update', methods=['PUT'])
@use_args(UpdateProductSchema, location="json")
def update_product(args):
    """
    This method is used for upadating preexisting product

    :param : id of product
    :param : name of product
    :param : company of product
    :param : formula of product
    :param : minimum quantity
    :param : distributor id 

    """
    print("here")
    
    try:
        result = Productblc.update_product(args)
        return jsonify({"response": "your product has been updated successfully"})
    except Exception as e:
        print(e)
        return jsonify({"error": e.args[0]}), HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/product/delete", methods=["DELETE"])
@use_args({"name": fields.Str(required=True)}, location="query")
def delete_product(args):
    try:
        product = ProductRepository.get_product_by_name(**args)
        db.session.delete(product)
        db.session.commit()
        return jsonify({"respose": "your product  has been deleted"})
    except Exception as e:
        print(e)
        return jsonify({"erorr": e.args[0]}), HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/product/getID", methods=["GET"])
@use_args({"name": fields.Str(required=True)}, location=True)
def get_id_by_name(name):
    id = ProductRepository.get_id_by_name(name)


@bp.route("/product/namelist", methods=["GET"])
@use_args({"name": fields.Str(required=True)}, location="query")
def get_list(name):
    # breakpoint()
    # lst = ProductRepository.get_list_by_name(**name)
    # schema = AddProductSchema(only=["name"], many=True)
    # result = schema.dump(lst)
    # post_result = Productblc.modify_name_of_list(result)
    # return jsonify(post_result)

    list_of_all_product_names = ProductRepository.get_list_of_all_product_names()
    result = get_close_matches(name["name"], list_of_all_product_names)
    return jsonify(result)


@bp.route("/product/distributors", methods=["GET"])
def get_distributors():
    result = Productblc.get_distributors_join()
    schema = ProductDistributorsSchema(many=True)
    res = schema.dump(result)
    return jsonify(res), 200