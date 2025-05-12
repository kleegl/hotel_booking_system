from abc import ABC

from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from repository.base_repository import BaseRepository, IBaseRepository
from schemas.user_schema import (
    UserCreateSchema,
    UserUpdateSchema,
    BaseSchema,
)


class IUserRepository(IBaseRepository[User, BaseSchema], ABC):
    pass


class UserRepository(IUserRepository, BaseRepository[User, BaseSchema]):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, User)

    async def create(self, item: UserCreateSchema) -> User:
        return await super().create(item)

    async def update(self, id: int, item: UserUpdateSchema) -> User:
        return await super().update(id, item)

    async def delete(self, id: int) -> None:
        return await super().delete(id)

    async def get(self, id: int) -> User | None:
        return await super().get(id)
