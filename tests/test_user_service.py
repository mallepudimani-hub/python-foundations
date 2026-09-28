from python_foundations.user_models import UserCreate
from python_foundations.user_service import UserValidationError, create_user


def test_create_user_returns_user_response() -> None:
    user = UserCreate(name="John Doe", email="john.doe@example.com", age=25)
    response = create_user(user)
    assert response.name == user.name
    assert response.email == user.email
    assert response.age == user.age


def test_create_user_raises_validation_error_for_underage_user() -> None:
    user = UserCreate(name="Jane Doe", email="jane.doe@example.com", age=17)
    try:
        create_user(user)
        assert False, "Expected UserValidationError to be raised"
    except UserValidationError as e:
        assert str(e) == "User must be at least 18 years old."
