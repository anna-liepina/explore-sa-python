from peewee import CharField, DoubleField
from .utils import BaseModel

class Marker(BaseModel):
    lat = DoubleField()
    lng = DoubleField()
    type = CharField()
    label = CharField()

    class Meta:
        db_table = 'markers'
