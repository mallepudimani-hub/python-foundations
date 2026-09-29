from python_foundations.user_models import UserCreate, UserResponse


class UserValidationError(Exception):
    """Raised when user business validation fails."""


class UserService:
    def create_user(self, user: UserCreate) -> UserResponse:
        if user.age < 18:
            raise UserValidationError("User must be at least 18 years old.")
        return UserResponse(
            name=user.name,
            email=user.email,
            age=user.age,
        )


def get_user_service() -> UserService:
    return UserService()
