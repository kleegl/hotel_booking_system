from response.base_response import BaseResponse


class BaseHotelRequest(BaseResponse):
    name: str
    location: str
    base_price: float
    capacity: int


class BaseHotelResponse(BaseResponse):
    id: int
    name: str
    location: str
    base_price: float
    capacity: int


class CreateHotelResponse(BaseHotelResponse):
    pass


class UpdateHotelResponse(BaseHotelResponse):
    name: str | None
    location: str | None
    base_price: float | None
    capacity: int | None
