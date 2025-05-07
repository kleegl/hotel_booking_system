from fastapi import APIRouter

hotel_router = APIRouter(prefix="/hotel", tags=["hotel"])


@hotel_router.get("/")
async def get_hotel():
    return "hotel"
