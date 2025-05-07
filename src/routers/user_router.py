from fastapi import APIRouter


user_router = APIRouter(prefix="/user", tags=["user"])


@user_router.get("/")
async def get_user():
    return "user"
