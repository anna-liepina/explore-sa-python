import strawberry

@strawberry.type
class Postcode:
    lat: float
    lng: float
    postcode: str
    lsoa: str
