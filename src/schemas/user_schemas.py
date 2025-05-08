from schemas.base_schema import BaseSchema


class BaseUserSchema(BaseSchema):
    name: str
    email: str
    phone_number: str
    password_hash: str


class CreateUserSchema(BaseUserSchema):
    pass


class UpdateUserSchema(BaseUserSchema):
    name: str | None
    email: str | None
    phone_number: str | None
    password_hash: str | None
