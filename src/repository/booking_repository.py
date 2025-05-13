from abc import ABC
from typing import Type

from models import Booking
from repository.base_repository import BaseRepository, IBaseRepository
from sqlalchemy.ext.asyncio import AsyncSession

from schemas.base_schema import BaseSchema
from schemas.booking_schema import (
    BookingCreateSchema,
    BookingUpdateSchema,
)


class IBookingRepository(IBaseRepository[Booking, BaseSchema], ABC):
    pass


class BookingRepository(
    IBookingRepository,
    BaseRepository[Booking, BaseSchema],
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Booking)

    async def create(self, item: BookingCreateSchema) -> Booking:
        return await super().create(item)

    async def update(self, item: BookingUpdateSchema) -> Booking:
        return await super().update(id, item)

    async def delete(self, id: int) -> None:
        return await super().delete(id)

    async def get(self, id: int) -> Booking | None:
        return await super().get_by_id(id)
