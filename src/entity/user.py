from typing import Any
from sqlalchemy import Column, Dialect, String, TypeDecorator
from sqlalchemy.orm import Relationship, Mapped
from exceptions.validation import ValidationException
from entity.base_entity import BaseEntity
import re


class EmailType(TypeDecorator):
    impl = String

    def process_bind_param(self, value: Any | None, dialect: Dialect) -> Any:
        if value:
            if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", value):
                raise ValidationException("Неверный формат email")
        return value


class PhoneType(TypeDecorator):
    impl = String

    def process_bind_param(self, value: Any | None, dialect: Dialect) -> Any:
        if value:
            if not re.match(r"^\+?\d{10,15}$", value):
                raise ValidationException("Неверный формат номера телефона")
        return value


class User(BaseEntity):
    name = Column(String, nullable=False)
    email = Column(EmailType, nullable=False)
    password_hash = Column(String, nullable=False)
    phone_number = Column(PhoneType, nullable=False)
    bookings: Mapped["Booking"] = Relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
