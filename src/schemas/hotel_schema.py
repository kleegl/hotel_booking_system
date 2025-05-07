from schemas.base_schema import BaseSchema


class BaseHotelSchema(BaseSchema):
    def __init__(self, name: str, location: str, base_price: float, capacity: int):
        self.name = name
        self.location = location
        self.base_price = base_price
        self.capacity = capacity


class HotelCreateSchema(BaseHotelSchema):
    def __init__(
        self, id: int | None, name: str, location: str, base_price: float, capacity: int
    ) -> None:
        super().__init__(name, location, base_price, capacity)
        self.id = id


class HotelUpdateSchema(BaseHotelSchema):
    def __init__(
        self, name: str, location: str, base_price: float, capacity: int
    ) -> None:
        super().__init__(name, location, base_price, capacity)
