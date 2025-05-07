from datetime import datetime
from entity.booking import BookingStatus
from schemas.base_schema import BaseSchema


class BaseBookingSchema(BaseSchema):
    def __init__(
        self,
        user_id: int,
        hotel_id: int,
        check_in: datetime,
        check_out: datetime,
        total_price: float,
        status: BookingStatus,
    ) -> None:
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.check_in = check_in
        self.check_out = check_out
        self.total_price = total_price
        self.status = status


class BookingCreateSchema(BaseBookingSchema):
    def __init__(
        self,
        id: int | None,
        user_id: int,
        hotel_id: int,
        check_in: datetime,
        check_out: datetime,
        total_price: float,
        status: BookingStatus,
    ) -> None:
        super().__init__(user_id, hotel_id, check_in, check_out, total_price, status)
        self.id = id


class BookingUpdateSchema(BaseBookingSchema):
    def __init__(
        self,
        user_id: int,
        hotel_id: int,
        check_in: datetime,
        check_out: datetime,
        total_price: float,
        status: BookingStatus,
    ) -> None:
        super().__init__(user_id, hotel_id, check_in, check_out, total_price, status)
