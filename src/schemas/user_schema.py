from schemas.base_schema import BaseSchema


class UserCreateSchema(BaseSchema):
    name: str
    email: str
    password_hash: str
    phone_number: str


class UserUpdateSchema(BaseSchema):
    name: str | None = None
    email: str | None = None
    password_hash: str | None = None
    phone_number: str | None = None


class UserResponseSchema(BaseSchema):
    id: int
    name: str | None = None
    email: str | None = None
    password_hash: str | None = None
    phone_number: str | None = None
