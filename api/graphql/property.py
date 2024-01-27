import typing
import strawberry
from .transaction import Transaction
from .postcode import Postcode
from ..orm import Property as PropertyORM

@strawberry.type
class Property:
    @strawberry.field
    @staticmethod
    async def type(parent: strawberry.Parent[PropertyORM]) -> str:
        return parent.propertyType
    @strawberry.field
    @staticmethod
    async def form(parent: strawberry.Parent[PropertyORM]) -> str:
        return parent.propertyForm
    @strawberry.field
    @staticmethod
    async def address(parent: strawberry.Parent[PropertyORM]) -> str:
        return ', '.join(filter(bool, [str(parent.street), parent.paon, parent.saon]))
    @strawberry.field
    @staticmethod
    async def postcode(parent: strawberry.Parent[PropertyORM]) -> Postcode:
        return Postcode(
            postcode= parent.postcode,
            lsoa= 'lsoa',
            lat= 50,
            lng= 50
        )
    @strawberry.field
    @staticmethod
    async def transactions(parent: strawberry.Parent[PropertyORM]) -> typing.List[Transaction]:
        return (
            [
                Transaction(date='01-01-2024', price=10000)
            ]
        )
