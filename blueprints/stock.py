
from unittest import result
from flask import Blueprint, jsonify
from webargs.flaskparser import use_args
from app.repositories.ProductRepository import ProductRepository
from app.schemas.StockSchema import GetStockSchema, StockSchema, StockRetrieveSchema
from app.repositories.StockRepository import StockRepository
from marshmallow import fields
from app.bl.StockBLC import StockBLC



bp = Blueprint("stock", __name__)

@bp.route("/stock/add", methods=["POST"])
@use_args(StockSchema, location="json")
def add_stock(stock:dict):
    """
    This method is used for adding stock of preexisting product

    :param price: price of new stock
    :param expiry: expiry of new stock
    :param quantity: quantity of new stock
    :param product_id: id of its product
    """
    added_stock = StockRepository.add_stock(stock)
    schema = StockSchema()
    result = schema.dump(added_stock)
    return jsonify(result)

@bp.route("/stock/all", methods=["GET"])
def get_all_stocks():

    all_stocks = StockRepository.all_stocks()
    schema = GetStockSchema(many=True)
    result = schema.dump(all_stocks)
    return jsonify(result)


@bp.route("/stock/retrieve", methods=["GET"])
@use_args({"name": fields.Str(required=True)}, location="query")
def get_stock(name):
    """
    This name is used for getting stock info

    :param name: name of stock's product
    """
    product_id = ProductRepository.get_id_by_name(**name)
    stock = StockRepository.get_stock_by_product_id(product_id)
    schema = StockRetrieveSchema(many=True)
    result = schema.dump(stock)
    post_result = StockBLC.add_extra_info(result, name)
    return jsonify(post_result)


