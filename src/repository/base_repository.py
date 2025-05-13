from abc import ABC, abstractmethod
from typing import Generic, Type
from sqlalchemy.ext.asyncio import AsyncSession

from generics import TBaseEntity, TSchema


class IBaseRepository(Generic[TBaseEntity, TSchema], ABC):
    @abstractmethod
    async def create(self, item: TSchema) -> TBaseEntity:
        NotImplementedError()

    @abstractmethod
    async def update(self, id: int, item: TSchema) -> TBaseEntity:
        NotImplementedError()

    @abstractmethod
    async def delete(self, id: int) -> None:
        NotImplementedError()

    @abstractmethod
    async def get_by_id(self, id: int) -> TBaseEntity | None:
        NotImplementedError()


class BaseRepository(IBaseRepository, Generic[TBaseEntity, TSchema]):
    def __init__(self, session: AsyncSession, model: Type[TBaseEntity]) -> None:
        self.session = session
        self.model = model

    async def create(self, item: TSchema) -> TBaseEntity:
        entity = self.model(**item.model_dump())
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def update(self, id: int, item: TSchema) -> TBaseEntity:
        db_item = await self.session.get(self.model, id)
        if not db_item:
            raise ValueError(f"{self.model.__name__} with id {id} not found")

        for field, value in item.model_dump(exclude_unset=True).items():
            setattr(db_item, field, value)

        await self.session.commit()
        await self.session.refresh(db_item)
        return db_item

    async def delete(self, id: int) -> None:
        result = await self.session.get(self.model, id)
        if result:
            await self.session.delete(result)
            await self.session.commit()

    async def get_by_id(self, id: int) -> TBaseEntity | None:
        return await self.session.get(self.model, id)
