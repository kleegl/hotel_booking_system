import pytest

from src.entity.user import User
from src.repository.user_repository import UserCreateSchema, UserRepository


@pytest.fixture
def init():
    pass


def test_create_user(init):
    user_to_db = UserCreateSchema(1, "name", "qwe@mail.ru", "89999234234", [1,2,3])
    user_from_db = User(1, "name", "qwe@mail.ru", "89999234234", None)
    
    user_repository = UserRepository()
    user_repository.create(user_to_db)
    
    assert user_from_db == user_from_db
    
    
    
    