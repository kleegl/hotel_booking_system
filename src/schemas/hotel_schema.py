from schemas.base_schema import BaseSchema


class BaseHotelSchema(BaseSchema):
    name: str
    location: str
    base_price: float
    capacity: int


class CreateHotelSchema(BaseHotelSchema):
    pass


class UpdateHotelSchema(BaseHotelSchema):
    pass


class HotelQuery(BaseHotelSchema):
    pass
