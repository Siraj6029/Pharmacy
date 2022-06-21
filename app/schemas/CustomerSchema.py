from pyexpat import model
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.repositories.models import Customer


class CustomerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Customer