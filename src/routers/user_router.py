from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import DatabaseSession
from repository.user_repository import UserRepository, IUserRepository
from schemas.user_schema import UserCreateSchema, UserUpdateSchema, UserResponseSchema


user_router = APIRouter(prefix="/user", tags=["user"])
database = DatabaseSession()


def get_repositroy(db: AsyncSession = Depends(database.get_db)) -> IUserRepository:
    return UserRepository(db)


@user_router.get("/{id}", response_model=UserResponseSchema)
async def get_by_id(id: int, repository: IUserRepository = Depends(get_repositroy)):
    user = await repository.get_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponseSchema.model_validate(user)


@user_router.post("/create", response_model=UserResponseSchema)
async def create(
    cretae_user_request: UserCreateSchema,
    repository: IUserRepository = Depends(get_repositroy),
):
    user = await repository.create(cretae_user_request)
    return user


@user_router.patch("/update", response_model=UserResponseSchema)
async def update(
    id: int,
    update_user_request: UserUpdateSchema,
    repository: IUserRepository = Depends(get_repositroy),
):
    user = await repository.update(id, update_user_request)
    return user


@user_router.delete("/delete")
async def delete(id: int, repository: IUserRepository = Depends(get_repositroy)):
    await repository.delete(id)
