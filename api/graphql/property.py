import typing
import strawberry
from .transaction import Transaction
from .postcode import Postcode

@strawberry.type
class Property:
    address: str
    type: str
    form: str
    postcode: Postcode
    transactions: typing.List[Transaction]
