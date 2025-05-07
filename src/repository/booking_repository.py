from abc import ABC

from entity.booking import Booking
from repository.base_repository import BaseRepository, IBaseRepository
from schemas.booking_schema import BookingCreateSchema, BookingUpdateSchema


class IBookingRepository(
    IBaseRepository[Booking, BookingCreateSchema, BookingUpdateSchema], ABC
):
    pass


class BookingRepositroy(
    IBookingRepository,
    BaseRepository[Booking, BookingCreateSchema, BookingUpdateSchema],
):
    def create(self, item: BookingCreateSchema) -> None:
        return super().create(item)

    def update(self, item: BookingUpdateSchema) -> None:
        return super().update(item)

    def delete(self, id: int) -> None:
        return super().delete(id)

    def get(self, id: int) -> Booking | None:
        return super().get(id)

    def _map_to_entity(self, booking: BookingCreateSchema) -> Booking:
        return Booking(
            id=booking.id,
            user_id=booking.user_id,
            hotel_id=booking.hotel_id,
            check_in=booking.check_in,
            check_out=booking.check_out,
            total_price=booking.total_price,
            status=booking.status,
        )

    def _update_entity(self, db_booking: Booking, booking: BookingUpdateSchema) -> None:
        db_booking.user_id = booking.user_id
        db_booking.hotel_id = booking.hotel_id
        db_booking.check_in = booking.check_in
        db_booking.total_price = booking.total_price
        db_booking.status = booking.status
