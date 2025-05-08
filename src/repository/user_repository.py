from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from entity.user import User
from repository.base_repository import BaseRepository, IBaseRepository
from schemas.user_schemas import CreateUserSchema, UpdateUserSchema


class IUserRepository(IBaseRepository[User, CreateUserSchema, UpdateUserSchema], ABC):
    pass


class UserRepository(
    IUserRepository, BaseRepository[User, CreateUserSchema, UpdateUserSchema]
):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session, User)

    async def create(self, item: CreateUserSchema) -> None:
        return await super().create(item)

    async def update(self, id: int, item: UpdateUserSchema) -> None:
        return await super().update(id, item)

    async def delete(self, id: int) -> None:
        return await super().delete(id)

    async def get(self, id: int) -> User | None:
        return await super().get(id)

    def _update_entity(self, db_user: User, user: UpdateUserSchema) -> None:
        if user.name:
            db_user.name = user.name
        if user.email:
            db_user.email = user.email
        if user.phone_number:
            db_user.phone_number = user.phone_number
        if user.password_hash:
            db_user.password_hash = user.password_hash
