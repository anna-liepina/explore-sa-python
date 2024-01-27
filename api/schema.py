from enum import Enum
import typing
import strawberry
from .graphql.marker import Marker
from .graphql.incident import Incident
from .graphql.postcode import Postcode
from .graphql.property import Property
from .graphql.transaction import Transaction
from .graphql.area import Area
from .graphql.timeline import Timeline
from . import orm as ORM

@strawberry.input
class GeoPoint:
    lat: float
    lng: float

@strawberry.enum
class RangeUnit(Enum):
    km = "km"
    ml = "ml"

@strawberry.type
class Query:
    @strawberry.field
    async def markerSearchInRange(
        pos: GeoPoint,
        range: float = 1,
        rangeUnit: RangeUnit = "km",
        perPage: int = 100,
        page: int = 1,
    ) -> typing.List[Marker]:
        offset = (page - 1) * perPage
        range /= 100

        minLat = pos.lat - range
        maxLat = pos.lat + range
        minLng = pos.lng - range
        maxLng = pos.lng + range

        return (
            ORM.Marker.select()
                .where(ORM.Marker.lat.between(lo = minLat, hi = maxLat))
                .where(ORM.Marker.lng.between(lo = minLng, hi = maxLng))
                .limit(perPage)
                .offset(offset)
                .execute()
        )

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
        offset = (page - 1) * perPage
        range /= 100

        minLat = pos.lat - range
        maxLat = pos.lat + range
        minLng = pos.lng - range
        maxLng = pos.lng + range

        return (
            ORM.Incident.select()
                .where(ORM.Incident.lat.between(lo = minLat, hi = maxLat))
                .where(ORM.Incident.lng.between(lo = minLng, hi = maxLng))
                .limit(perPage)
                .offset(offset)
                .execute()
        )

    @strawberry.field
    async def postcodeSearch(
        pattern: str,
        perPage: int = 100,
        page: int = 1,
    ) -> typing.List[Postcode]:
        offset = (page - 1) * perPage
        query = (
            ORM.Postcode.select()
                .where(ORM.Postcode.postcode.contains(pattern))
                .limit(perPage)
                .offset(offset)
        )

        return query.execute()

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
        offset = (page - 1) * perPage
        
        query = (
            ORM.Transaction.select()
                .where(ORM.Transaction.guid.contains(postcodePattern))
                .limit(perPage)
                .offset(offset)
        )

        if dateFrom:
            query = (
                query
                    .where(ORM.Transaction.date.__ge__(dateFrom))
            )

        if dateTo:
            query = (
                query
                    .where(ORM.Transaction.date.__le__(dateTo))
            )

        return query.execute()

    @strawberry.field
    async def timelineSearch(
        postcodePattern: str,
        postcodes: typing.List[str],
        dateFrom: typing.Optional[str] = None,
        dateTo: typing.Optional[str] = None,
        perPage: int = 100,
        page: int = 1
    ) -> typing.List[Timeline]:
        offset = (page - 1) * perPage
        query = (
            ORM.Timeline.select()
                .limit(perPage)
                .offset(offset)
        )

        if postcodePattern:
            query = (
                query
                    .where(ORM.Timeline.postcode.contains(postcodePattern))
            )

        if postcodes:
            query = (
                query
                    .where(ORM.Timeline.postcode.in_(postcodes))
            )

        if dateFrom:
            query = (
                query
                    .where(ORM.Timeline.date.__ge__(dateFrom))
            )

        if dateTo:
            query = (
                query
                    .where(ORM.Timeline.date.__le__(dateTo))
            )

        return query.execute()

    @strawberry.field
    async def areaSearch(
        postcodePattern: str,
        perPage: int = 100,
        page: int = 1,
    ) -> typing.List[Area]:
        offset = (page - 1) * perPage

        return (
            ORM.Area.select()
                .where(ORM.Area.area.contains(postcodePattern))
                .limit(perPage)
                .offset(offset)
                .execute()
        )

schema = strawberry.Schema(query=Query)
