from datetime import datetime
from models import BookingStatus
from schemas.base_schema import BaseSchema


class BookingCreateSchema(BaseSchema):
    user_id: int
    hotel_id: int
    room_id: int
    check_in: datetime
    check_out: datetime
    total_price: float
    status: BookingStatus


class BookingUpdateSchema(BaseSchema):
    user_id: int
    hotel_id: int
    room_id: int
    check_in: datetime
    check_out: datetime
    total_price: float
    status: BookingStatus


class BookingResponseSchema(BaseSchema):
    id: int
    user_id: int
    hotel_id: int
    room_id: int
    check_in: datetime
    check_out: datetime
    total_price: float
    status: BookingStatus
