from peewee import Model, CharField
from .utils import BaseModel

class Area(BaseModel):
    area = CharField(primary_key=True, max_length=4)
    city = CharField()

    class Meta:
        db_table = 'areas'
