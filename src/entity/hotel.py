from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from entity.base_entity import BaseEntity


class Hotel(BaseEntity):
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    base_price = Column(Float, nullable=False, doc="цена за ночь")
    capacity = Column(Integer, nullable=False, doc="количество доступных номеров")

    CheckConstraint("base_price > 0", name="valid_base_price")
    CheckConstraint("capacity >= 0", name="valid_capacity")
