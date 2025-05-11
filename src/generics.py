from typing import TypeVar
from models import BaseEntity
from response.base_response import BaseResponse


TBaseEntity = TypeVar("TBaseEntity", bound=BaseEntity)
TCreateResponse = TypeVar("TCreateResponse", bound=BaseResponse)
TUpdateResponse = TypeVar("TUpdateResponse", bound=BaseResponse)
