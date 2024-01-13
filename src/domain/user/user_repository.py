from abc import ABC, abstractmethod
from typing import Optional

from src.domain.user import user


class UserRepository(ABC):
    @abstractmethod
    def insert(self, user: user.User) -> None:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[user.User]:
        raise NotImplementedError

    @abstractmethod
    def find_by_username(self, username: str) -> Optional[user.User]:
        raise NotImplementedError
