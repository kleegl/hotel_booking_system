import random

from entity.base_entity import BaseEntity


class User(BaseEntity):
    def __init__(self, id: int| None, name: str, email: str, phone_number: str, booking_ids: list[int] | None) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.booking_ids: list[int] = []
        
        
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int | None) -> None:
        if id != None:
            self._id = id
        else:
            self._id = random.randint(1, 1000)