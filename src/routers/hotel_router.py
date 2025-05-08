from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends

from database.db import DatabaseSession
from repository.hotel_repository import IHotelRepository, HotelRepository
from schemas.hotel_schema import CreateHotelSchema, UpdateHotelSchema

hotel_router = APIRouter(prefix="/hotel", tags=["hotel"])
database = DatabaseSession()


def get_repository(db: AsyncSession = Depends(database.get_db)) -> IHotelRepository:
    return HotelRepository(db)


@hotel_router.get("/{id}")
async def get_by_id(
    id: int,
    repository: IHotelRepository = Depends(get_repository),
):
    hotel = await repository.get_by_id(id)
    return hotel


@hotel_router.post("/create")
async def create(
    create_hotel_schema: CreateHotelSchema,
    repository: IHotelRepository = Depends(get_repository),
) -> CreateHotelSchema:
    result = await repository.create(create_hotel_schema)
    return result


@hotel_router.patch("/update")
async def update(
    id: int,
    update_hotel_schema: UpdateHotelSchema,
    repository: IHotelRepository = Depends(get_repository),
):
    await repository.update(id, update_hotel_schema)


@hotel_router.delete("/delete/{id}")
async def delete(
    id: int,
    repository: IHotelRepository = Depends(get_repository),
):
    await repository.delete(id)
