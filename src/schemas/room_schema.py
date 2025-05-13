from models import RoomType
from schemas.base_schema import BaseSchema


class RoomCreateSchema(BaseSchema):
    hotel_id: int
    type: RoomType
    price_per_night: float
    capacity: int


class RoomUpdateSchema(BaseSchema):
    type: RoomType | None = None
    price_per_night: float | None = None
    capacity: int | None = None


class RoomResponseSchema(BaseSchema):
    id: int
    hotel_id: int | None = None
    type: RoomType | None = None
    price_per_night: float | None = None
    capacity: int | None = None
