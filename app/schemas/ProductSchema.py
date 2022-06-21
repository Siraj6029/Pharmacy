from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.schemas.DistributorSchema import DistributorSchema
from app.repositories.models.Product import Product
from marshmallow import fields, Schema, post_dump


class GetProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
    distributor = fields.Nested(DistributorSchema(only=("name",)))


class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
    distributor = fields.Nested(DistributorSchema(only=("name",)))

    @post_dump
    def onlyDictName(self, data, **kwargs):
        # breakpoint()
        new_data = data.copy()
        if "distributor" in new_data.keys() and new_data["distributor"]:
            new_data["distributor"] = new_data["distributor"]["name"]

        return new_data

    
        
class AddProductSchema(Schema):
    name = fields.Str(required=True)
    company = fields.Str(required=True)
    formula = fields.Str(required=True)
    minQuantity = fields.Int(required=False)
    distributor_id =  fields.Int(required=False)


class UpdateProductSchema(Schema):
    # class Meta:
        # model = Product

    id = fields.Int(required=True)
    name = fields.Str(required=False)
    company = fields.Str(required=False)
    formula = fields.Str(required=False)
    minQuantity = fields.Int(required=False)
    distributor_id =  fields.Int(required=False)


class ProductAllSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product

class ProductDistributorsSchema(SQLAlchemyAutoSchema):
    product = fields.Nested(ProductAllSchema)
    distributor = fields.Nested(DistributorSchema)