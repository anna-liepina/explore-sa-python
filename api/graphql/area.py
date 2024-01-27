import strawberry
from .. import orm as ORM

@strawberry.type
class Area:
    area: str
    city: str
