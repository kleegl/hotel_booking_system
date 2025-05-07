from schemas.base_schema import BaseSchema


class BaseUserSchema(BaseSchema):
    def __init__(
        self, name: str, email: str, phone_number: str, booking_ids: list[int] | None
    ) -> None:
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.booking_ids = booking_ids


class UserCreateSchema(BaseUserSchema):
    def __init__(
        self,
        id: int | None,
        name: str,
        email: str,
        phone_number: str,
        booking_ids: list[int] | None,
    ) -> None:
        super().__init__(email, name, phone_number, booking_ids)
        self.id = id


class UserUpdateSchema(BaseUserSchema):
    def __init__(
        self, name: str, email: str, phone_number: str, booking_ids: list[int] | None
    ) -> None:
        super().__init__(email, name, phone_number, booking_ids)
