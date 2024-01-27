from peewee import CharField, IntegerField, ForeignKeyField
from api.orm.postcode import Postcode
from .utils import BaseModel

class Property(BaseModel):
    guid = CharField(unique=True)
    postcode = CharField(max_length=9)
    # postcode = ForeignKeyField(Postcode, backref='postcode')
    propertyType = CharField(max_length=1)
    propertyForm = CharField(max_length=1)
    paon = CharField()
    saon = CharField()
    street = CharField()
    city = CharField()

    class Meta:
        db_table = 'properties'
