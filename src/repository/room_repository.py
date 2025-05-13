from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession

from models import Room
from repository.base_repository import BaseRepository, IBaseRepository
from schemas.base_schema import BaseSchema
from schemas.room_schema import RoomCreateSchema, RoomUpdateSchema


class IRoomRepository(IBaseRepository[Room, BaseSchema], ABC):
    pass


class RoomRepository(IRoomRepository, BaseRepository[Room, BaseSchema]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, Room)

    async def create(self, item: RoomCreateSchema) -> Room:
        return await super().create(item)

    async def update(self, id: int, item: RoomUpdateSchema) -> Room:
        return await super().update(id, item)

    async def detele(self, id: int) -> None:
        return await super().delete(id)

    async def get_by_id(self, id: int) -> Room | None:
        return await super().get_by_id(id)
