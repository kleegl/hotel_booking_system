from schemas.base_schema import BaseSchema


class HotelCreateSchema(BaseSchema):
    name: str
    location: str
    base_price: float
    capacity: int


class HotelUpdateSchema(BaseSchema):
    name: str | None = None
    location: str | None = None
    base_price: float | None = None
    capacity: int | None = None


class HotelResponseSchema(BaseSchema):
    id: int
    name: str | None = None
    location: str | None = None
    base_price: float | None = None
    capacity: int | None = None
