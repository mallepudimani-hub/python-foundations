from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from python_foundations.db_models import User


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, user: User) -> User:
        self.db.add(user)
        # self.db.commit()
        # self.db.refresh(user)
        return user

    def get_all(self) -> list[User]:
        return self.db.query(User).all()

    def get_by_id(self, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)
        result = self.db.execute(statement)
        return result.scalar_one_or_none()

    def update_age(self, user_id: int, age: int) -> bool:
        statement = (
            update(User).where(User.id == user_id).values(age=age).returning(User.id)
        )

        result = self.db.execute(statement)
        updated_id = result.scalar_one_or_none()

        if updated_id is None:
            self.db.rollback()
            return False

        self.db.commit()
        return True

    def delete_user(self, user_id: int) -> bool:
        statement = delete(User).where(User.id == user_id).returning(User.id)

        result = self.db.execute(statement)
        deleted_id = result.scalar_one_or_none()

        if deleted_id is None:
            self.db.rollback()
            return False

        self.db.commit()
        return True
