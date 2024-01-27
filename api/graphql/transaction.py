import strawberry

@strawberry.type
class Transaction:
    price: int
    date: str
    # property: Property
