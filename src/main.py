import uvicorn
from fastapi import FastAPI

from routers import hotel_router, room_router, user_router, booking_router

app = FastAPI()

app.include_router(hotel_router)
app.include_router(user_router)
app.include_router(room_router)
app.include_router(booking_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
