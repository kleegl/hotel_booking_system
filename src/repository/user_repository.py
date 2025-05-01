from abc import ABC, abstractmethod

from entity.user import User
from repository.base_repository import BaseRepository, IBaseRepository
from schemas.user_schemas import UserCreateSchema, UserUpdateSchema


class IUserRepository(IBaseRepository[User, UserCreateSchema, UserUpdateSchema], ABC):
    pass


class UserRepository(IUserRepository, BaseRepository[User, UserCreateSchema, UserUpdateSchema]):
    def create(self, item: UserCreateSchema) -> None:
        return super().create(item)
    
    
    def update(self, item: UserUpdateSchema) -> None:
        return super().update(item)
    
    
    def delete(self, id: int) -> None:
        return super().delete(id)
    
    
    def get(self, id: int) -> User | None:
        return super().get(id)
    
    
    def _map_to_entity(self, user: UserCreateSchema) -> User:
        return User(id=user.id, name=user.name, email=user.email, phone_number=user.phone_number, booking_ids=user.booking_ids)


    def _update_entity(self, db_user: User, user: UserUpdateSchema) -> None:
        db_user.name = user.name
        db_user.email = user.email 
        db_user.phone_number = user.phone_number 
        db_user.booking_ids = user.booking_ids