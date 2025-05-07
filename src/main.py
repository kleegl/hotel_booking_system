import uvicorn
from fastapi import FastAPI

from routers.hotel_router import hotel_router
from routers.user_router import user_router
from routers.booking_router import booking_router

app = FastAPI()

app.include_router(hotel_router)
app.include_router(user_router)
app.include_router(booking_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
