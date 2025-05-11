from response.base_response import BaseResponse


class BaseUserResponse(BaseResponse):
    name: str
    email: str
    phone_number: str
    password_hash: str


class CreateUserResponse(BaseUserResponse):
    pass


class UpdateUserResponse(BaseUserResponse):
    name: str | None
    email: str | None
    phone_number: str | None
    password_hash: str | None
