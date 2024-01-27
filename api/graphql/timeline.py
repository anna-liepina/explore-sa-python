import strawberry

@strawberry.type
class Timeline:
    date: str
    avg: int
    count: int
    postcode: str
