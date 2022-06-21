from pyexpat import model
from unicodedata import name
from marshmallow import post_dump
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields
# from marshmallow import fields, validates, ValidationError
from app.repositories.models.Stock import Stock
from app.schemas.ProductSchema import GetProductSchema

class StockSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Stock
        include_fk = True
    #     exclude = ("expiry",)
    
    # expiry = fields.Date(required = True)

    # @validates("expiry")
    # def validate_quantity(self, value):
    #     breakpoint()
        # if value < 0:
        #     raise ValidationError("Quantity must be greater than 0.")
        # if value > 30:
        #     raise ValidationError("Quantity must not be greater than 30.")

class GetStockSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Stock
    product= fields.Nested(GetProductSchema(only=("name",)))

    @post_dump
    def get_stock(self, data, **kwargs):
        copied_data = data.copy()
        if copied_data["product"]:
            copied_data["product"] = copied_data["product"]["name"]
        return copied_data


class StockRetrieveSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Stock