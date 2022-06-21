from http import HTTPStatus
from flask import Blueprint, jsonify
from app.repositories.DistributorRepository import DistributorRepository
from app.schemas.DistributorSchema import AddDistributorSchema, DistributorSchema
from app.repositories.db import db
from webargs.flaskparser import use_args
from webargs import fields
from app.bl.DistrubutorBLC import Distributorblc


bp = Blueprint("Distributor", __name__)

@bp.route('/distributor/add', methods=['POST'])
@use_args(AddDistributorSchema, location="json")
def add_distributor(distributor:dict):
    """
    This method is used to add a new distributor

    :param name: name of Distributor
    :param contact: contact of distributor
    :param address: address of distributor
    return: object
    """
    print("here")
    try:

        distributor_created = DistributorRepository.add_distributor(distributor)

        schema = DistributorSchema()
        result = schema.dump(distributor_created)
        return jsonify(result), HTTPStatus.OK
    
    except Exception as e:
        print(e)
        return jsonify({"error": e.args[0]}), HTTPStatus.UNPROCESSABLE_ENTITY
        

@bp.route('/distributor/getidbyname', methods=['GET'])
@use_args({"name": fields.Str(required=True)}, location="query")
def get_distID_by_distName(args:dict):

    """
    This method is used to get Distributor id by its name for adding product

    :param name: name of Distributor
    """

    try:
        print(type(args))
        distributor = DistributorRepository.get_id_by_name(**args) 
        schema = DistributorSchema(only=('id',))
        result = schema.dump(distributor)
        return jsonify(result), HTTPStatus.OK

    except Exception as e:
        print(e)
        return jsonify({"error": e.args}), HTTPStatus.UNPROCESSABLE_ENTITY

# @use_args({"name": fields.Str(required=True)}, location="query")
@bp.route('/distributor/all', methods=['GET'])
def get_all_dist():
    """
    This method is used to get all distributors

    :param : no parameter is passed 
    """
    try:
        distributors = DistributorRepository.getAllDist()
        schema = DistributorSchema(many=True)
        result = schema.dump(distributors)
        return jsonify(result), HTTPStatus.OK
        # Top line internally becomes like below
        # distributors = DistributorRepository.get_all_dist(name='Siraj')
    except Exception as e:
        print(e)
        return jsonify({"error": e.args[0]}), HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/distributor/retrieve", methods=["GET"])
@use_args({"name": fields.Str(required=True)}, location="query")
def get_distributor(args:dict):
    """
    this method is used to get distributor one by one by its name

    :param name: name of distributor
    return object
    """
    try:
        dist = DistributorRepository.get_dist(**args)
        schema = DistributorSchema()
        result = schema.dump(dist)
        return jsonify(result), HTTPStatus.OK
    except Exception as e:
        print(e)
        return jsonify({"error": e.args[0]}), HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/distributor/update", methods=["PUT"])
@use_args(DistributorSchema, location="json")
def modify_distribution(args:dict):
    """
    This method is used to modify pre-existing distributor

    :param name: name of Distributor
    :param contact: contact of distributor
    :param address: address of distributor
    return: object
    """
    
    try:
        distribution_to_be_updated = Distributorblc.update_distributor(args)
        return jsonify({"Message": 'your distributor has been successfuly updated'})
    except Exception as e:
        print(e)
        return jsonify({"error": e.args[0]}), HTTPStatus.UNPROCESSABLE_ENTITY
        

@bp.route("/distributor/delete", methods=["DELETE"])
@use_args({"name": fields.Str(required=True)}, location="query")
def delete_distributor(args:dict):
    
    """
    This method is used to delete distributor by name

    :param : name of distributor
    """
    try:
        distr = DistributorRepository.get_dist(**args)
        db.session.delete(distr)
        db.session.commit()
        return jsonify({"Message": ' This Distributor has been deleted successfuly'})
    except Exception as e:
        print(e)
        return jsonify({"error": e.args[0]}), HTTPStatus.UNPROCESSABLE_ENTITY 
