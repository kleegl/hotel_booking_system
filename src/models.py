import enum
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    Enum,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import as_declarative, declared_attr, Relationship


class BookingStatus(enum.Enum):
    PENDING = 0
    CONFIRM = 1
    CANCEL = 2
    COMPLETE = 3


class RoomType(enum.Enum):
    NA = "N/A"
    STANDARD = "STANDARD"
    LUX = "LUX"


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


class Hotel(BaseEntity):
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    rooms = Relationship("Room", back_populates="hotel", cascade="all, delete-orphan")


class Booking(BaseEntity):
    user_id = Column(ForeignKey("users.id"))
    user = Relationship("User")
    hotel_id = Column(ForeignKey("hotels.id"))
    hotel = Relationship("Hotel")
    room_id = Column(ForeignKey("rooms.id"))
    room = Relationship("Room")
    check_in = Column(DateTime(timezone=True), doc="дата и время заезда")
    check_out = Column(DateTime(timezone=True), doc="дата и время выезда")
    total_price = Column(Float, nullable=False, doc="общая стоимость бронирования")
    status = Column(
        Enum(BookingStatus, name="booking_status"),
        nullable=False,
        default=BookingStatus.PENDING,
        doc="статус заявки",
    )


class Room(BaseEntity):
    hotel_id = Column(ForeignKey("hotels.id"))
    hotel = Relationship("Hotel", back_populates="rooms")
    type = Column(
        Enum(RoomType, name="room_type"),
        nullable=False,
        default=RoomType.NA,
        doc="тип номера",
    )
    price_per_night = Column(Float, nullable=False)
    capacity = Column(Integer, nullable=False)
    is_available = Column(Boolean, default=True)
