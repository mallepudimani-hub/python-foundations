from sqlalchemy import select
from sqlalchemy.orm import Session

from python_foundations.db_models import User


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_all(self) -> list[User]:
        return self.db.query(User).all()

    def get_by_id(self, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)
        result = self.db.execute(statement)
        return result.scalar_one_or_none()
