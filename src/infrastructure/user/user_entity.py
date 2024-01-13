from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.domain.user import user
from src.infrastructure.common.base_model import BaseModel


class UserEntity(BaseModel):
    __tablename__ = "user_entities"

    username: Mapped[str] = mapped_column(String(255), index=True, unique=True, nullable=False)
    hash_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(255), nullable=False)

    def to_model(self) -> user.User:
        return user.recreate_user(self.id, self.username, self.hash_password, self.role)


def new_user_entity(u: user.User) -> UserEntity:
    return UserEntity(id=u.id, username=u.username, hash_password=u.hash_password, role=u.role.type.value)
