from peewee import CharField, IntegerField
from .utils import BaseModel

class Transaction(BaseModel):
    date = CharField()
    avg = IntegerField()
    count =  IntegerField()
    postcode = CharField()

    class Meta:
        db_table = 'transactions'
