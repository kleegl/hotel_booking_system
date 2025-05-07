from sqlalchemy import CheckConstraint, Column, DateTime, Float, Enum, ForeignKey
from sqlalchemy.orm import Relationship, Mapped
from entity.base_entity import BaseEntity
import enum


class BookingStatus(enum.Enum):
    PENDING = 0
    CONFIRM = 1
    CANCEL = 2
    COMPLETE = 3


class Booking(BaseEntity):
    user_id = Column(ForeignKey("users.id"))
    user: Mapped["User"] = Relationship(back_populates="bookings")
    hotel_id = Column(ForeignKey("hotels.id"))
    hotel: Mapped["Hotel"] = Relationship(back_populates="bookings")
    check_in = Column(DateTime(timezone=True), doc="дата и время заезда")
    check_out = Column(DateTime(timezone=True), doc="дата и время выезда")
    total_price = Column(Float, nullable=False, doc="общая стоимость бронирования")
    status = Column(
        Enum(BookingStatus, name="booking_status"),
        nullable=False,
        default=BookingStatus.PENDING,
        doc="статус заявки",
    )

    CheckConstraint("check_out > check_in", name="valid_dates")
    CheckConstraint("total_price > 0", name="valid_total_price")
