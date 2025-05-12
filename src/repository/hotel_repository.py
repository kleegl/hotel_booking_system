from abc import ABC

from models import Hotel
from repository.base_repository import BaseRepository, IBaseRepository

from sqlalchemy.ext.asyncio import AsyncSession
from schemas.hotel_schema import HotelCreateSchema, HotelUpdateSchema, BaseSchema


class IHotelRepository(IBaseRepository[Hotel, BaseSchema], ABC):
    pass


class HotelRepository(IHotelRepository, BaseRepository[Hotel, BaseSchema]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Hotel)

    async def create(self, item: HotelCreateSchema) -> Hotel:
        return await super().create(item)

    async def update(self, id: int, item: HotelUpdateSchema) -> Hotel:
        return await super().update(id, item)

    async def delete(self, id: int) -> None:
        return await super().delete(id)

    async def get_by_id(self, id: int) -> Hotel | None:
        return await super().get_by_id(id)
