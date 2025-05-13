from typing import Type

from fastapi import APIRouter, Depends, HTTPException
from database.db import DatabaseSession
from generics import TBaseEntity, TSchema
from repository.base_repository import IBaseRepository
from sqlalchemy.ext.asyncio import AsyncSession

from repository.hotel_repository import HotelRepository
from repository.room_repository import RoomRepository
from repository.user_repository import UserRepository
from repository.booking_repository import BookingRepository

from schemas.booking_schema import (
    BookingResponseSchema,
    BookingCreateSchema,
    BookingUpdateSchema,
)
from schemas.hotel_schema import (
    HotelResponseSchema,
    HotelCreateSchema,
    HotelUpdateSchema,
)
from schemas.room_schema import RoomResponseSchema, RoomCreateSchema, RoomUpdateSchema
from schemas.user_schema import UserResponseSchema, UserCreateSchema, UserUpdateSchema


def create_router(
    prefix: str,
    response_model: Type[TBaseEntity],
    create_model: Type[TSchema],
    update_model: Type[TSchema],
    repository_type: Type[IBaseRepository[TBaseEntity, TSchema]],
) -> APIRouter:
    router = APIRouter(prefix=f"/{prefix}", tags=[prefix])

    def get_repository(
        db: AsyncSession = Depends(DatabaseSession().get_db),
    ) -> IBaseRepository[TBaseEntity, TSchema]:
        return repository_type(db)

    @router.get("/{id}", response_model=response_model)
    async def get_by_id(
        id: int,
        repository: IBaseRepository[TBaseEntity, TSchema] = Depends(get_repository),
    ):
        item = await repository.get_by_id(id)
        if item is None:
            raise HTTPException(
                status_code=404, detail=f"{prefix.capitalize()} not found"
            )
        return response_model.model_validate(item)

    @router.post("/create", response_model=response_model)
    async def create(
        item: create_model,
        repository: IBaseRepository[TBaseEntity, TSchema] = Depends(get_repository),
    ):
        response_item = await repository.create(item)
        return response_item

    @router.patch("/update", response_model=response_model)
    async def update(
        id: int,
        item: update_model,
        repository: IBaseRepository[TBaseEntity, TSchema] = Depends(get_repository),
    ):
        response_item = await repository.update(id, item)
        return response_item

    @router.delete("/delete")
    async def delete(
        id: int,
        repository: IBaseRepository[TBaseEntity, TSchema] = Depends(get_repository),
    ):
        await repository.delete(id)

    return router


hotel_router = create_router(
    prefix="hotels",
    response_model=HotelResponseSchema,
    create_model=HotelCreateSchema,
    update_model=HotelUpdateSchema,
    repository_type=HotelRepository,
)

room_router = create_router(
    prefix="rooms",
    response_model=RoomResponseSchema,
    create_model=RoomCreateSchema,
    update_model=RoomUpdateSchema,
    repository_type=RoomRepository,
)

user_router = create_router(
    prefix="users",
    response_model=UserResponseSchema,
    create_model=UserCreateSchema,
    update_model=UserUpdateSchema,
    repository_type=UserRepository,
)


booking_router = create_router(
    prefix="bookings",
    response_model=BookingResponseSchema,
    create_model=BookingCreateSchema,
    update_model=BookingUpdateSchema,
    repository_type=BookingRepository,
)
