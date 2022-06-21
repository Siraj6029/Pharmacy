from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.repositories.models.Distributor import Distributor
from marshmallow import fields, post_load

class DistributorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Distributor


class AddDistributorSchema(SQLAlchemyAutoSchema):
    name = fields.Str(required=True)
    address = fields.Str(required=False)
    contact = fields.Str(required=False)

    # @post_load
    # def create_distributor(self, data, **kwargs):
    #     return Distributor(**data)
