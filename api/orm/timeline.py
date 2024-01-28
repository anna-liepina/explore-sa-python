from peewee import CharField, IntegerField
from .utils import BaseModel

class Timeline(BaseModel):
    date = CharField()
    avg = IntegerField()
    count =  IntegerField()
    postcode = CharField()

    class Meta:
        db_table = 'timelines'
