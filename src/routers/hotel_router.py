from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, status

from database.db import DatabaseSession
from repository.hotel_repository import IHotelRepository, HotelRepository
from response.hotel_response import (
    BaseHotelRequest,
    BaseHotelResponse,
    CreateHotelResponse,
    UpdateHotelResponse,
)

hotel_router = APIRouter(prefix="/hotel", tags=["hotel"])
database = DatabaseSession()


def get_repository(db: AsyncSession = Depends(database.get_db)) -> IHotelRepository:
    return HotelRepository(db)


@hotel_router.get("/{id}", response_model=BaseHotelResponse)
async def get_by_id(
    id: int,
    repository: IHotelRepository = Depends(get_repository),
):
    hotel = await repository.get_by_id(id)
    if hotel is None:
        return status.HTTP_404_NOT_FOUND
    return BaseHotelResponse.model_validate(hotel)


@hotel_router.post("/create")
async def create(
    create_hotel_request: BaseHotelRequest,
    repository: IHotelRepository = Depends(get_repository),
) -> CreateHotelResponse:
    result = await repository.create(create_hotel_request)
    return result


@hotel_router.patch("/update")
async def update(
    id: int,
    update_hotel_Response: UpdateHotelResponse,
    repository: IHotelRepository = Depends(get_repository),
):
    await repository.update(id, update_hotel_Response)


@hotel_router.delete("/delete/{id}")
async def delete(
    id: int,
    repository: IHotelRepository = Depends(get_repository),
):
    await repository.delete(id)
