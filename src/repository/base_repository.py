from abc import ABC, abstractmethod
from typing import Generic, Type
from sqlalchemy.ext.asyncio import AsyncSession

from generics import TBaseEntity, TCreateSchema, TUpdateSchema


class IBaseRepository(Generic[TBaseEntity, TCreateSchema, TUpdateSchema], ABC):
    @abstractmethod
    async def create(self, item: TCreateSchema) -> TCreateSchema:
        NotImplementedError()

    @abstractmethod
    async def update(self, id: int, item: TUpdateSchema) -> TUpdateSchema:
        NotImplementedError()

    @abstractmethod
    async def delete(self, id: int) -> None:
        NotImplementedError()

    @abstractmethod
    async def get(self, id: int) -> TBaseEntity:
        NotImplementedError()


class BaseRepository(
    IBaseRepository, Generic[TBaseEntity, TCreateSchema, TUpdateSchema]
):
    def __init__(self, session: AsyncSession, model: Type[TBaseEntity]) -> None:
        self.session = session
        self.model = model

    async def create(self, item: TCreateSchema) -> TCreateSchema:
        entity = self.model(**item.model_dump())
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def update(self, id: int, item: TUpdateSchema) -> TUpdateSchema:
        result = await self.session.get(TBaseEntity, id)
        if result:
            self._update_entity(result, item)
            # await self.session.commit()
        return result

    async def delete(self, id: int) -> None:
        result = await self.session.get(TBaseEntity, id)
        if result:
            self.session.delete(result)
            # self.session.commit()

    async def get(self, id: int) -> TBaseEntity:
        return await self.session.get(TBaseEntity, id)

    @abstractmethod
    def _update_entity(
        self, db_item: TBaseEntity, update_item: TUpdateSchema
    ) -> None: ...
