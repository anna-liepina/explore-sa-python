from peewee import CharField, IntegerField
from .utils import BaseModel

class Property(BaseModel):
    guid = CharField(unique=True)
    postcode = CharField(max_length=9)
    propertyType = CharField(max_length=1)
    propertyForm = CharField(max_length=1)
    paon = CharField()
    saon = CharField()
    street = CharField()
    city = CharField()

    class Meta:
        db_table = 'properties'
