
from http import HTTPStatus
import json
from unittest import result
from flask import Blueprint, jsonify
from marshmallow import ValidationError
from webargs.flaskparser import use_args
from app.schemas.CustomerSchema import CustomerSchema
from app.repositories.CustomerRepository import CustomerRepsitory
from webargs import fields
from app.repositories.db import db
# from app.bl.CustomerBLC import CustomerBLC

from app.schemas.ProductSchema import ProductSchema


bp = Blueprint("customer", __name__)

@bp.route("/customer/add", methods=["POST"])
@use_args(CustomerSchema, location="json")
def add_customer(args:dict):
    """
    this method
    """
    try:
        customer = CustomerRepsitory.add_customer(args)
        schema = CustomerSchema()
        result = schema.dump(customer)
        return jsonify(result)
    except Exception as e:
        print(e)
        return jsonify({"erorr": e.args[0]}), HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/customer/all", methods=["GET"])
def get_all_customer():
    customers = CustomerRepsitory.get_all_customers()
    schema = CustomerSchema(many=True)
    result = schema.dump(customers)
    return jsonify(result)


@bp.route("/customer/retrieve", methods=["GET"])
@use_args({"name": fields.Str(required=True)}, location="query")
def get_customer(args):
    customer = CustomerRepsitory.get_customer_by_name(**args)
    # breakpoint()
    if not customer:
        return jsonify({"error": "customer not found"}), 422
    schema = CustomerSchema(many=True)
    result = schema.dump(customer)
    return jsonify(result)


@bp.route("/customer/update", methods=["PUT"])
@use_args(CustomerSchema, location="json")
def update_customer(customer:dict):
    try:
        updated_customer = CustomerRepsitory.update_customer(customer)
        schema = CustomerSchema()
        result = schema.dump(updated_customer)
        return jsonify(result)
    except ValidationError as e:
        return jsonify({"Error": e.messages[0]}), 422


@bp.route("/customer/delete", methods=["DELETE"])
@use_args({"name": fields.Str(required=True)}, location="query")
def delete_customer(customer_name:dict):
    try:
        customer = CustomerRepsitory.get_customer_by_name(**customer_name)
        db.session.delete(customer)
        db.session.commit()
        return jsonify({"error": "customer has been deleted successfully"})
    except Exception as e:
        print(e)
        return jsonify({"error": e.args[0]}), 422