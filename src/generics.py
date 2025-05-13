from typing import TypeVar

from pydantic import BaseModel
from models import BaseEntity


TBaseEntity = TypeVar("TBaseEntity", bound=BaseEntity)
TSchema = TypeVar("TSchema", bound=BaseModel)
