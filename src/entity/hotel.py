import random


class Hotel:
    def __init__(self, id: int | None, name: str, location: str, base_price: float, capacity: int) -> None:
        self.id = id
        self.name = name
        self.location = location
        self.base_price = base_price #цена за ночь
        self.capacity = capacity #количество доступных номеров
        
        
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int | None) -> None:
        if id != None:
            self._id = id
        else:
            self._id = random.randint(1, 1000)