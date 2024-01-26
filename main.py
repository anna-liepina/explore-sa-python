from enum import Enum
import typing
import strawberry
from strawberry.asgi import GraphQL
from fastapi import FastAPI

@strawberry.input
class GeoPoint:
    lat: float
    lng: float

@strawberry.enum
class RangeUnit(Enum):
    km = "km"
    ml = "ml"

@strawberry.type
class Area:
    area: str
    city: str

@strawberry.type
class Incident:
    lat: float
    lng: float
    type: str
    date: str
    outcome: str

@strawberry.type
class Marker:
    lat: float
    lng: float
    type: str
    label: str

@strawberry.type
class Postcode:
    lat: float
    lng: float
    lsoa: str
    postcode: str

@strawberry.type
class Transaction:
    price: int
    date: str
    # property: Property

@strawberry.type
class Timeline:
    date: str
    avg: int
    count: int
    postcode: str

@strawberry.type
class Property:
    address: str
    type: str
    form: str
    postcode: Postcode
    transactions: typing.List[Transaction]

@strawberry.type
class Query:
    @strawberry.field
    async def propertySearchInRange(
        pos: GeoPoint,
        range: float = 1,
        rangeUnit: RangeUnit = "km",
        perPage: int = 100,
        page: int = 1,
    ) -> typing.List[Property]:
        return []

    @strawberry.field
    async def incidentSearchInRange(
        pos: GeoPoint,
        range: float = 1,
        rangeUnit: RangeUnit = "km",
        perPage: int = 100,
        page: int = 1,
    ) -> typing.List[Incident]:
        return []

    @strawberry.field
    async def markerSearchInRange(
        pos: GeoPoint,
        range: float = 1,
        rangeUnit: RangeUnit = "km",
        perPage: int = 100,
        page: int = 1,
    ) -> typing.List[Marker]:
        return []

    @strawberry.field
    async def postcodeSearch(
        pattern: str,
        perPage: int = 100,
        page: int = 1,
    ) -> typing.List[Postcode]:
        return []

    @strawberry.field
    async def propertySearch(
        postcodePattern: str,
        dateFrom: typing.Optional[str] = None,
        dateTo: typing.Optional[str] = None,
        perPage: int = 100,
        page: int = 1
    ) -> typing.List[Property]:
        return []

    @strawberry.field
    async def transactionSearch(
        postcodePattern: str,
        dateFrom: typing.Optional[str] = None,
        dateTo: typing.Optional[str] = None,
        perPage: int = 100,
        page: int = 1
    ) -> typing.List[Transaction]:
        return []

    @strawberry.field
    async def timelineSearch(
        postcodePattern: str,
        postcodes: typing.List[str],
        dateFrom: typing.Optional[str] = None,
        dateTo: typing.Optional[str] = None,
        perPage: int = 100,
        page: int = 1
    ) -> typing.List[Timeline]:
        return []

    @strawberry.field
    async def areaSearch(
        postcodePattern: str,
        perPage: int = 100,
        page: int = 1,
    ) -> typing.List[Area]:
        return []

schema = strawberry.Schema(query=Query)

app = FastAPI()

@app.get("/")
def index():
    return {"message": "index"}

app.add_route("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)