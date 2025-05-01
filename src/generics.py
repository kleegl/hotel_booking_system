from typing import TypeVar
from entity.base_entity import BaseEntity
from schemas.base_schema import BaseSchema


TBaseEntity = TypeVar('TBaseEntity', bound=BaseEntity)
TCreateSchema = TypeVar('TCreateSchema', bound=BaseSchema)
TUpdateSchema = TypeVar('TUpdateSchema', bound=BaseSchema)