from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import DatabaseSession
from repository.user_repository import IUserRepository, UserRepository
from schemas.user_schemas import CreateUserSchema, UpdateUserSchema


user_router = APIRouter(prefix="/user", tags=["user"])
database = DatabaseSession()


def get_repositroy(db: AsyncSession = Depends(database.get_db)) -> IUserRepository:
    return UserRepository(db)


@user_router.get("/")
async def get_by_id(id: int, repository: IUserRepository = Depends(get_repositroy)):
    result = await repository.get_by_id(id)
    return result


@user_router.post("/create")
async def create(
    cretae_user_schema: CreateUserSchema,
    repository: IUserRepository = Depends(get_repositroy),
):
    result = await repository.create(cretae_user_schema)
    return result


@user_router.patch("/update")
async def update(
    id: int,
    update_user_schema: UpdateUserSchema,
    repository: IUserRepository = Depends(get_repositroy),
):
    await repository.update(id, update_user_schema)


@user_router.delete("/delete")
async def delete(id: int, repository: IUserRepository = Depends(get_repositroy)):
    await repository.delete(id)
