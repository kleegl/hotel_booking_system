from abc import ABC

from entity.hotel import Hotel
from repository.base_repository import BaseRepository, IBaseRepository
from schemas.hotel_schema import CreateHotelSchema, UpdateHotelSchema

from sqlalchemy.ext.asyncio import AsyncSession


class IHotelRepository(
    IBaseRepository[Hotel, CreateHotelSchema, UpdateHotelSchema], ABC
):
    pass


class HotelRepository(
    IHotelRepository, BaseRepository[Hotel, CreateHotelSchema, UpdateHotelSchema]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Hotel)

    async def create(self, item: CreateHotelSchema) -> Hotel:
        return await super().create(item)

    async def update(self, id: int, item: UpdateHotelSchema) -> UpdateHotelSchema:
        return await super().update(id, item)

    async def delete(self, id: int) -> None:
        return await super().delete(id)

    async def get(self, id: int) -> Hotel | None:
        return await super().get(id)

    def _update_entity(self, db_hotel: Hotel, hotel: UpdateHotelSchema) -> None:
        db_hotel.name = hotel.name
        db_hotel.location = hotel.location
        db_hotel.base_price = hotel.base_price
        db_hotel.capacity = hotel.capacity
