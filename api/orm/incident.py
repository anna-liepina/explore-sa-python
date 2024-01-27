from peewee import CharField, DoubleField
from .utils import BaseModel

class Incident(BaseModel):
    lat = DoubleField()
    lng = DoubleField()
    type = CharField(null=True)
    date = CharField()
    outcome = CharField(null=True)

    class Meta:
        db_table = 'incidents'
