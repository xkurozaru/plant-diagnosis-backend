from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from src.domain.user import user, user_repository
from src.infrastructure.user import user_entity


class UserDatabase(user_repository.UserRepository):
    def __init__(self, session: Session) -> None:
        self.__session: Session = session

    def insert(self, u: user.User) -> None:
        try:
            u_e = user_entity.new_user_entity(u)
            self.__session.add(u_e)
            self.__session.commit()
        except Exception as e:
            self.__session.rollback()
            raise e

    def find_by_id(self, id: str) -> Optional[user.User]:
        try:
            u_e = self.__session.query(user_entity.UserEntity).filter_by(id=id).one()
            return u_e.to_model()
        except NoResultFound:
            return None
        except Exception as e:
            raise e

    def find_by_username(self, username: str) -> Optional[user.User]:
        try:
            u_e = self.__session.query(user_entity.UserEntity).filter_by(username=username).one()
            return u_e.to_model()
        except NoResultFound:
            return None
        except Exception as e:
            raise e
