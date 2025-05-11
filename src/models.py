import enum
from sqlalchemy import (
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import as_declarative, declared_attr, Relationship


@as_declarative()
class BaseEntity:
    id = Column(Integer, primary_key=True, index=True)

    @declared_attr
    def __tablename__(cls):
        return "".join([cls.__name__.lower(), "s"])


class User(BaseEntity):
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    bookings = Relationship("Booking", back_populates="user")


class Hotel(BaseEntity):
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    base_price = Column(Float, nullable=False, doc="цена за ночь")
    capacity = Column(Integer, nullable=False, doc="количество доступных номеров")
    bookings = Relationship("Booking", back_populates="hotel")


class BookingStatus(enum.Enum):
    PENDING = 0
    CONFIRM = 1
    CANCEL = 2
    COMPLETE = 3


class Booking(BaseEntity):
    user_id = Column(ForeignKey("users.id"))
    user = Relationship("User", back_populates="bookings")
    hotel_id = Column(ForeignKey("hotels.id"))
    hotel = Relationship("Hotel", back_populates="bookings")
    check_in = Column(DateTime(timezone=True), doc="дата и время заезда")
    check_out = Column(DateTime(timezone=True), doc="дата и время выезда")
    total_price = Column(Float, nullable=False, doc="общая стоимость бронирования")
    status = Column(
        Enum(BookingStatus, name="booking_status"),
        nullable=False,
        default=BookingStatus.PENDING,
        doc="статус заявки",
    )
