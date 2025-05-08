from schemas.base_schema import BaseSchema


class BaseHotelSchema(BaseSchema):
    name: str
    location: str
    base_price: float
    capacity: int


class CreateHotelSchema(BaseHotelSchema):
    pass


class UpdateHotelSchema(BaseHotelSchema):
    name: str | None
    location: str | None
    base_price: float | None
    capacity: int | None


class HotelQuery(BaseHotelSchema):
    pass
