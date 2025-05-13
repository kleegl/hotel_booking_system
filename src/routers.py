from typing import Type

from fastapi import APIRouter, Depends, HTTPException
from database.db import DatabaseSession
from generics import TBaseEntity, TSchema
from repository.base_repository import IBaseRepository
from sqlalchemy.ext.asyncio import AsyncSession

from repository.hotel_repository import HotelRepository
from repository.room_repository import RoomRepository
from repository.user_repository import UserRepository
from schemas.base_schema import BaseSchema
from schemas.hotel_schema import HotelResponseSchema
from schemas.room_schema import RoomResponseSchema
from schemas.user_schema import UserResponseSchema


def create_router(
    prefix: str,
    response_model: Type[TBaseEntity],
    schema: Type[TSchema],
    repository_type: Type[IBaseRepository[TBaseEntity, TSchema]],
    database: DatabaseSession,
) -> APIRouter:
    router = APIRouter(prefix=f"/{prefix}", tags=[prefix])

    def get_repository(
        db: AsyncSession = Depends(database.get_db),
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
        item: schema,
        repository: IBaseRepository[TBaseEntity, TSchema] = Depends(get_repository),
    ):
        response_item = await repository.create(item)
        return response_item

    @router.patch("/update", response_model=response_model)
    async def update(
        id: int,
        item: schema,
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
    schema=BaseSchema,
    repository_type=HotelRepository,
    database=DatabaseSession(),
)

room_router = create_router(
    prefix="rooms",
    response_model=RoomResponseSchema,
    schema=BaseSchema,
    repository_type=RoomRepository,
    database=DatabaseSession(),
)

user_router = create_router(
    prefix="users",
    response_model=UserResponseSchema,
    schema=BaseSchema,
    repository_type=UserRepository,
    database=DatabaseSession(),
)
