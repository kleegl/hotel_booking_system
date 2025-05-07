from fastapi import APIRouter


booking_router = APIRouter(prefix="/booking", tags=["booking"])


@booking_router.get("/")
async def get_booking():
    return "booking"
