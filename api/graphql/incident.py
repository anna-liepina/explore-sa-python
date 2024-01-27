import strawberry
import typing

@strawberry.type
class Incident:
    lat: float
    lng: float
    date: str
    type: typing.Optional[str]
    outcome: typing.Optional[str]
