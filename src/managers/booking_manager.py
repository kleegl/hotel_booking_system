from repository.booking_repository import IBookingRepository
from repository.hotel_repository import IHotelRepository
from repository.user_repository import IUserRepository
from schemas.booking_schema import BookingCreateSchema


class BookingManager:
    def __init__(
        self,
        user_repository: IUserRepository,
        hotel_repositroy: IHotelRepository,
        booking_repository: IBookingRepository,
    ) -> None:
        self.user_repository = user_repository
        self.hotel_repositroy = hotel_repositroy
        self.booking_repository = booking_repository

    def create_booking(self, schema: BookingCreateSchema) -> None:
        user = self.user_repository.get(schema.user_id)
        if user == None:
            raise ValueError(f"Пользователь с id = {id} не найден")
        hotel = self.hotel_repositroy.get(schema.hotel_id)
        if hotel == None:
            raise ValueError(f"Отель с id = {id} не найден")

        self.booking_repository.create(schema)
