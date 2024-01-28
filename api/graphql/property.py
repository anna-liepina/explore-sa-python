import typing
import strawberry
from strawberry.dataloader import DataLoader
from .transaction import Transaction
from .postcode import Postcode
from ..orm import Property as PropertyORM, Postcode as PostcodeORM, Transaction as TransactionORM

async def batchPostcodeLoad(keys: typing.List[str]) -> typing.List[Postcode]:
    postcodes = (
        PostcodeORM
            .select()
            .where(PostcodeORM.postcode.in_(keys))
            .execute()
    )

    return [Postcode(**postcode.__data__) for postcode in postcodes]

async def batchTransactionLoad(keys: typing.List[str]) -> typing.List[typing.List[Transaction]]:
    transactions = (
        TransactionORM
            .select()
            .where(TransactionORM.guid.in_(keys))
            .execute()
    )
    
    cache = {}
    for t in transactions:
        key = t.guid;
        cache[key] = cache.get(key, [])
        fields = { field: getattr(t, field) for field in Transaction.__annotations__.keys() }
        cache[key].append(Transaction(**fields))
        
    return [cache.get(key, None) for key in keys]

postcodeLoader = DataLoader(load_fn=batchPostcodeLoad)
transactionLoader = DataLoader(load_fn=batchTransactionLoad)

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
        return await postcodeLoader.load(parent.postcode)
    @strawberry.field
    @staticmethod
    async def transactions(parent: strawberry.Parent[PropertyORM]) -> typing.List[Transaction]:
        return await transactionLoader.load(parent.guid)
