from src.domain.user.user import User, new_member_user
from src.domain.user.user_repository import UserRepository


class AccountApplicationService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.__user_repository: UserRepository = user_repository

    def sign_up(self, username: str, password: str) -> User:
        user = new_member_user(username, password)
        self.__user_repository.insert(user)

        return user

    def sign_in(self, username: str, password: str) -> User:
        user = self.__user_repository.find_by_username(username)
        if user is None:
            raise Exception("User not found")

        if not user.is_valid_password(password):
            raise Exception("Invalid password")

        return user

    def get_user(self, user_id: str) -> User:
        user = self.__user_repository.find_by_id(user_id)
        if user is None:
            raise Exception("User not found")

        return user
