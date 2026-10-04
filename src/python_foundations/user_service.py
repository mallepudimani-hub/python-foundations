from fastapi import Depends
from sqlalchemy.orm import Session

from python_foundations.database import get_db
from python_foundations.db_models import User
from python_foundations.user_models import UserCreate, UserResponse
from python_foundations.user_repository import UserRepository


class UserValidationError(Exception):
    """Raised when user business validation fails."""


class UserService:
    def __init__(self, db: Session) -> None:
        self.repository = UserRepository(db)

    def create_user(self, user: UserCreate) -> UserResponse:
        if user.age < 18:
            raise UserValidationError("User must be at least 18 years old.")

        db_user = User(
            name=user.name,
            email=user.email,
            age=user.age,
        )

        db_user = self.repository.create(db_user)

        return UserResponse(
            name=db_user.name,
            email=db_user.email,
            age=db_user.age,
        )

    def get_users(self) -> list[UserResponse]:
        users = self.repository.get_all()
        return [
            UserResponse(name=user.name, email=user.email, age=user.age)
            for user in users
        ]


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)
