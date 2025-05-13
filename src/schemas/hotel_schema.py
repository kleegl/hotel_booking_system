from schemas.base_schema import BaseSchema


class HotelCreateSchema(BaseSchema):
    name: str
    location: str


class HotelUpdateSchema(BaseSchema):
    name: str | None = None
    location: str | None = None


class HotelResponseSchema(BaseSchema):
    id: int
    name: str | None = None
    location: str | None = None
