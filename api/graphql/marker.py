import strawberry

@strawberry.type
class Marker:
    lat: float
    lng: float
    type: str
    label: str
