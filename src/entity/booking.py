from datetime import datetime
import random
from enum import Enum


class BookingStatus(Enum):
    CONFIRM = 0
    CANCEL = 1
    COMPLETE = 2


#класс-сущность Бронирование
class Booking:
    def __init__(self, id: int | None, user_id: int, hotel_id: int, check_in: datetime, check_out: datetime, total_price: float, status: BookingStatus) -> None:
        self.id = id
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.check_in = check_in
        self.check_out = check_out
        self.total_price = total_price
        self.status = status
        
        
    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, id: int | None) -> None:
        if id != None:
            self._id = id
        else:
            self._id = random.randint(1, 1000)
    