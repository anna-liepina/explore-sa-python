from peewee import CharField, DoubleField
from .utils import BaseModel

class Postcode(BaseModel):
    lat = DoubleField()
    lng = DoubleField()
    postcode = CharField(primary_key=True)
    lsoa = CharField()

    class Meta:
        db_table = 'postcodes'

