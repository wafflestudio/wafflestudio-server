from fastapi import Depends
from sqlalchemy.orm import Session

from waffledotcom.src.database.connection import get_db_session
from waffledotcom.src.database.connection import Transaction
from waffledotcom.src.database.models import User


class UserRepository:
    def __init__(
        self,
        session: Session = Depends(get_db_session),
        transaction: Transaction = Depends(),
    ):
        self.session = session
        self.transaction = transaction

    def get_users(self) -> list[User]:
        return self.session.query(User).all()

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.session.query(User).filter(User.id == user_id).first()

    def get_user_by_sso_id(self, sso_id: str) -> User | None:
        return self.session.query(User).filter(User.sso_id == sso_id).first()

    def create_user(self, user: User) -> User:
        with self.transaction:
            self.session.add(user)
        return user

    def create_users(self, users: list[User]) -> None:
        with self.transaction:
            self.session.bulk_save_objects(users)

    def update_user(self, user: User) -> User | None:
        if self.get_user_by_id(user.id) is None:
            return None

        with self.transaction:
            self.session.merge(user)

        return user
