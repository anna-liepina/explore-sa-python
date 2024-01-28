import typing
import strawberry
from strawberry.dataloader import DataLoader
from .transaction import Transaction
from .postcode import Postcode
from ..orm import Property as PropertyORM, Postcode as PostcodeORM

# Now, you need to define a function to load the postcode data based on keys
async def batch_load_postcodes(keys: typing.List[str]) -> typing.List[Postcode]:
    print('keys', keys)
    # Assuming PostcodeORM has a method to fetch multiple postcodes by a list of keys
    postcode_records = (
        PostcodeORM
            .select()
            .where(PostcodeORM.postcode.in_(keys))
            .execute()
    )

    print('postcode_records', postcode_records);
    print('dicts', postcode_records.__dict__)
    # Convert database records to Postcode objects
    postcode_data = [Postcode(**record.__dict__) for record in postcode_records]

    # Return the postcode data in the same order as keys
    return postcode_data

postcode_loader = DataLoader(load_fn=batch_load_postcodes)

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
        postcode_data = await postcode_loader.load(parent.postcode)
        return postcode_data
    @strawberry.field
    @staticmethod
    async def transactions(parent: strawberry.Parent[PropertyORM]) -> typing.List[Transaction]:
        return (
            [
                Transaction(date='01-01-2024', price=10000)
            ]
        )
        