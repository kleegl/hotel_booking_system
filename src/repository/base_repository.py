from abc import ABC, abstractmethod
from typing import Generic

from extensions.db_list import DbList
from generics import TBaseEntity, TCreateSchema, TUpdateSchema


class IBaseRepository(Generic[TBaseEntity, TCreateSchema, TUpdateSchema], ABC):
    @abstractmethod
    def create(self, item: TCreateSchema) -> None:
        pass

    @abstractmethod
    def update(self, item: TUpdateSchema) -> None:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass

    @abstractmethod
    def get(self, id: int) -> TBaseEntity | None:
        pass


class BaseRepository(
    IBaseRepository, Generic[TBaseEntity, TCreateSchema, TUpdateSchema]
):
    __db: DbList[TBaseEntity] = DbList()

    def create(self, item: TCreateSchema):
        try:
            item_db = self._map_to_entity(item)
            self.__db.append(item_db)
        except:
            raise ValueError(f"Ошибка при создании объекта типа {type(TBaseEntity)}")

    def update(self, id: int, item: TUpdateSchema) -> None:
        item_from_db = self.__db.find_by_id(id)
        if item_from_db != None:
            self._update_entity(item_from_db, item)
        else:
            raise ValueError(f"Объект типа {type(TBaseEntity)} с id = {id} не найден")

    def delete(self, id: int) -> None:
        item_from_db = self.__db.find_by_id(id)
        if item_from_db != None:
            self.__db.remove(item_from_db)
        else:
            raise ValueError(f"Объект типа {type(TBaseEntity)} с id = {id} не найден")

    def get(self, id: int) -> TBaseEntity | None:
        return self.__db.find_by_id(id)

    @abstractmethod
    def _map_to_entity(self, item: TCreateSchema) -> TBaseEntity: ...

    @abstractmethod
    def _update_entity(
        self, db_item: TBaseEntity, update_item: TUpdateSchema
    ) -> None: ...
