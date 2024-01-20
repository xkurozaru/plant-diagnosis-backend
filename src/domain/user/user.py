import hashlib

from src.config import ITER, SALT
from src.domain.common import nano_id
from src.domain.user import role

MIN_USERNAME_LENGTH = 2
MAX_USERNAME_LENGTH = 32
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 72


class User:
    __id: str
    __username: str
    __hash_password: str
    __role: role.Role

    def __init__(self, id: str, username: str, hash_password: str, role: role.Role) -> None:
        self.__id = id
        self.__username = username
        self.__hash_password = hash_password
        self.__role = role

    @property
    def id(self) -> str:
        return self.__id

    @property
    def username(self) -> str:
        return self.__username

    @property
    def hash_password(self) -> str:
        return self.__hash_password

    @property
    def role(self) -> role.Role:
        return self.__role

    def is_valid_password(self, password: str) -> bool:
        return self.__hash_password == hash(password)


def hash(password: str) -> str:
    return hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), SALT.encode("utf-8"), int(ITER)).hex()


def new_member_user(username: str, password: str) -> User:
    if len(username) < MIN_USERNAME_LENGTH or len(username) > MAX_USERNAME_LENGTH:
        raise Exception(f"Username must be between {MIN_USERNAME_LENGTH} and {MAX_USERNAME_LENGTH} characters")

    if len(password) < MIN_PASSWORD_LENGTH or len(password) > MAX_PASSWORD_LENGTH:
        raise Exception(f"Password must be between {MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH} characters")

    return User(nano_id.generate(), username, hash(password), role.new_member_role())


def new_admin_user(username: str, password: str) -> User:
    if len(username) < MIN_USERNAME_LENGTH or len(username) > MAX_USERNAME_LENGTH:
        raise Exception(f"Username must be between {MIN_USERNAME_LENGTH} and {MAX_USERNAME_LENGTH} characters")

    if len(password) < MIN_PASSWORD_LENGTH or len(password) > MAX_PASSWORD_LENGTH:
        raise Exception(f"Password must be between {MIN_PASSWORD_LENGTH} and {MAX_PASSWORD_LENGTH} characters")

    return User(nano_id.generate(), username, hash(password), role.new_admin_role())


def recreate_user(id: str, username: str, hash_password: str, role_type: str) -> User:
    return User(id, username, hash_password, role.recreate_role(role_type))
