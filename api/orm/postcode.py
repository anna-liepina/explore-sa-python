from peewee import CharField, DoubleField
from .utils import BaseModel

class Postcode(BaseModel):
    lat = DoubleField()
    lng = DoubleField()
    postcode = CharField(primary_key=True, max_length=9)
    lsoa = CharField()

    class Meta:
        db_table = 'postcodes'

