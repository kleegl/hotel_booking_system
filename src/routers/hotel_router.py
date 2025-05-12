from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException, status

from database.db import DatabaseSession
from repository.hotel_repository import IHotelRepository, HotelRepository
from schemas.hotel_schema import (
    HotelResponseSchema,
    HotelCreateSchema,
    HotelUpdateSchema,
)

hotel_router = APIRouter(prefix="/hotel", tags=["hotel"])
database = DatabaseSession()


def get_repository(db: AsyncSession = Depends(database.get_db)) -> IHotelRepository:
    return HotelRepository(db)


@hotel_router.get("/{id}", response_model=HotelResponseSchema)
async def get_by_id(
    id: int,
    repository: IHotelRepository = Depends(get_repository),
):
    hotel = await repository.get_by_id(id)
    if hotel is None:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return HotelResponseSchema.model_validate(hotel)


@hotel_router.post("/create")
async def create(
    create_hotel_request: HotelCreateSchema,
    repository: IHotelRepository = Depends(get_repository),
) -> HotelResponseSchema:
    result = await repository.create(create_hotel_request)
    return result


@hotel_router.patch("/update", response_model=HotelResponseSchema)
async def update(
    id: int,
    update_hotel_Response: HotelUpdateSchema,
    repository: IHotelRepository = Depends(get_repository),
):
    result = await repository.update(id, update_hotel_Response)
    return result


@hotel_router.delete("/delete/{id}")
async def delete(
    id: int,
    repository: IHotelRepository = Depends(get_repository),
):
    await repository.delete(id)
