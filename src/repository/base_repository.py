from abc import ABC, abstractmethod
from typing import Generic, Type
from sqlalchemy.ext.asyncio import AsyncSession

from generics import TBaseEntity, TCreateResponse, TUpdateResponse


class IBaseRepository(Generic[TBaseEntity, TCreateResponse, TUpdateResponse], ABC):
    @abstractmethod
    async def create(self, item: TCreateResponse) -> TCreateResponse:
        NotImplementedError()

    @abstractmethod
    async def update(self, id: int, item: TUpdateResponse) -> TUpdateResponse:
        NotImplementedError()

    @abstractmethod
    async def delete(self, id: int) -> None:
        NotImplementedError()

    @abstractmethod
    async def get_by_id(self, id: int) -> TBaseEntity:
        NotImplementedError()


class BaseRepository(
    IBaseRepository, Generic[TBaseEntity, TCreateResponse, TUpdateResponse]
):
    def __init__(self, session: AsyncSession, model: Type[TBaseEntity]) -> None:
        self.session = session
        self.model = model

    async def create(self, item: TCreateResponse) -> TCreateResponse:
        entity = self.model(**item.model_dump())
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def update(self, id: int, item: TUpdateResponse) -> TUpdateResponse:
        result = await self.session.get(self.model, id)
        if result:
            self._update_entity(result, item)
            await self.session.commit()
        return result

    async def delete(self, id: int) -> None:
        result = await self.session.get(self.model, id)
        if result:
            await self.session.delete(result)
            await self.session.commit()

    async def get_by_id(self, id: int) -> TBaseEntity:
        return await self.session.get(self.model, id)

    @abstractmethod
    def _update_entity(
        self, db_item: TBaseEntity, update_item: TUpdateResponse
    ) -> None: ...
