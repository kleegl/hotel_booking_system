from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from sqlalchemy.orm import Mapped, Relationship
from entity.base_entity import BaseEntity


class Hotel(BaseEntity):
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    base_price = Column(Float, nullable=False, doc="цена за ночь")
    capacity = Column(Integer, nullable=False, doc="количество доступных номеров")
    bookings: Mapped["Booking"] = Relationship(back_populates="hotel")

    CheckConstraint("base_price > 0", name="valid_base_price")
    CheckConstraint("capacity >= 0", name="valid_capacity")
