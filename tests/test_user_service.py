from unittest.mock import Mock

import pytest

from python_foundations.db_models import User
from python_foundations.user_models import UserCreate, UserResponse
from python_foundations.user_service import UserService, UserValidationError


def test_create_user_returns_user_response() -> None:
    user = UserCreate(name="John Doe", email="john.doe@example.com", age=25)
    user_service = UserService(Mock())
    response = user_service.create_user(user)
    assert response.name == user.name
    assert response.email == user.email
    assert response.age == user.age


def test_create_user_raises_validation_error_for_underage_user() -> None:
    user = UserCreate(name="Jane Doe", email="jane.doe@example.com", age=17)
    user_service = UserService(Mock())
    try:
        user_service.create_user(user)
        assert False, "Expected UserValidationError to be raised"
    except UserValidationError as e:
        assert str(e) == "User must be at least 18 years old."


def test_update_user_age_returns_updated_user() -> None:
    repository = Mock()

    repository.update_age.return_value = True
    repository.get_by_id.return_value = User(
        id=1,
        name="Mani",
        email="mani@example.com",
        age=31,
    )

    service = UserService(Mock())
    service.repository = repository

    actual = service.update_user_age(1, 31)

    assert actual == UserResponse(
        name="Mani",
        email="mani@example.com",
        age=31,
    )


def test_update_user_age_returns_none_when_user_does_not_exist() -> None:
    repository = Mock()
    repository.update_age.return_value = False

    service = UserService(Mock())
    service.repository = repository

    actual = service.update_user_age(999, 31)

    assert actual is None
    repository.get_by_id.assert_not_called()


def test_delete_user_returns_true_when_user_exists() -> None:
    repository = Mock()
    repository.delete_user.return_value = True

    service = UserService(Mock())
    service.repository = repository

    actual = service.delete_user(1)

    assert actual is True
    repository.delete_user.assert_called_once_with(1)


def test_delete_user_returns_false_when_user_does_not_exist() -> None:
    repository = Mock()
    repository.delete_user.return_value = False

    service = UserService(Mock())
    service.repository = repository

    actual = service.delete_user(999)

    assert actual is False
    repository.delete_user.assert_called_once_with(999)


def test_create_user_rolls_back_when_repository_fails() -> None:
    db = Mock()
    service = UserService(db)

    service.repository = Mock()
    service.repository.create.side_effect = RuntimeError("Database error")

    user = UserCreate(
        name="Mani",
        email="mani@example.com",
        age=30,
    )

    with pytest.raises(RuntimeError, match="Database error"):
        service.create_user(user)

    db.rollback.assert_called_once()
    db.commit.assert_not_called()
