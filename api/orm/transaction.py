from peewee import CharField, IntegerField
from .utils import BaseModel

class Transaction(BaseModel):
    price = IntegerField()
    date = CharField()
    guid = CharField()

    class Meta:
        db_table = 'transactions'
