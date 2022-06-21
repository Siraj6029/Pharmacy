from marshmallow import ValidationError
from app.repositories.db import db
from app.repositories.models.Customer import Customer

class CustomerRepsitory:
    @staticmethod
    def add_customer(args):
        new_customer = Customer(**args) 
        db.session.add(new_customer)
        db.session.commit()
        return new_customer

    @staticmethod
    def get_all_customers():
        all_customers = Customer.query.all()
        return all_customers

    @staticmethod
    def get_customer_by_name(name):
        # customer = Customer.query.filter.like(name=name).all()
        # lst = Product.query.filter(Product.name.like(name+"%")).all()
        customer = Customer.query.filter(Customer.name.like("%"+name+"%")).all()
        return customer

    @staticmethod
    def get_customer_by_id(id):
        customer = Customer.query.filter_by(id=id).first()
        return customer

    @staticmethod
    def update_customer(customer:dict):  
        """
        :param id: id of customer 
        """
        existing_customer = CustomerRepsitory.get_customer_by_id(customer["id"])

        if existing_customer:
            existing_customer.name = customer["name"]
            existing_customer.address = customer["address"]
            db.session.commit()
            return existing_customer
        else:
            raise ValidationError("Customer not existing")
