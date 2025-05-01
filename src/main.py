

from managers.booking_manager import UserManager
from repository.user_repository import UserCreateSchema, UserRepository


if __name__ == "__main__":
    user_repository = UserRepository()
    
    # user_repository.create(UserCreateSchema(1, "name", "qwe", "123", None))
    # user_repository.create(UserCreateSchema(None, "name", "qwe", "123", None))
    # user_repository.get(1)
    # user_manager.create_user(UserCreateSchema(1, "name", "qwe", "123", None))