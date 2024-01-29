import strawberry
import typing

@strawberry.type
class Marker:
    lat: float
    lng: float
    type: str
    label: typing.Optional[str]
