from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database.db import DatabaseSession
from schemas.room_schema import RoomCreateSchema, RoomResponseSchema, RoomUpdateSchema
from repository.room_repository import IRoomRepository, RoomRepository


room_router = APIRouter(prefix="/rooms", tags=["rooms"])
database = DatabaseSession()


def get_repository(db: AsyncSession = Depends(database.get_db)) -> IRoomRepository:
    return RoomRepository(db)


@room_router.get("{id}", response_model=RoomResponseSchema)
async def get_by_id(id: int, repository: IRoomRepository = Depends(get_repository)):
    room = await repository.get_by_id(id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return RoomResponseSchema.model_validate(room)


@room_router.post("/create", response_model=RoomResponseSchema)
async def create(
    create_room_response: RoomCreateSchema,
    repository: IRoomRepository = Depends(get_repository),
):
    room = await repository.create(create_room_response)
    return room


@room_router.patch("/update", response_model=RoomResponseSchema)
async def update(
    id: int,
    update_room_response: RoomUpdateSchema,
    repository: IRoomRepository = Depends(get_repository),
):
    room = await repository.update(id, update_room_response)
    return room


@room_router.delete("/delete/{id}")
async def delete(id: int, repository: IRoomRepository = Depends(get_repository)):
    await repository.delete(id)
