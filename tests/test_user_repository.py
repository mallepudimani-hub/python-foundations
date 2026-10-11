from unittest.mock import Mock

from sqlalchemy import select

from python_foundations.db_models import User
from python_foundations.user_repository import UserRepository


def test_get_by_id_returns_user() -> None:
    db = Mock()

    user = User(
        id=1,
        name="Mani",
        email="mani@example.com",
        age=30,
    )

    result = Mock()
    result.scalar_one_or_none.return_value = user
    db.execute.return_value = result

    repository = UserRepository(db)

    actual = repository.get_by_id(1)

    assert actual is user
    db.execute.assert_called_once()

    statement = db.execute.call_args.args[0]

    assert str(statement) == str(select(User).where(User.id == 1))


def test_update_age_returns_true_when_user_exists() -> None:
    db = Mock()

    result = Mock()
    result.scalar_one_or_none.return_value = 1
    db.execute.return_value = result

    repository = UserRepository(db)

    actual = repository.update_age(1, 31)

    assert actual is True
    db.commit.assert_called_once()


def test_update_age_returns_false_when_user_does_not_exist() -> None:
    db = Mock()

    result = Mock()
    result.scalar_one_or_none.return_value = None
    db.execute.return_value = result

    repository = UserRepository(db)

    actual = repository.update_age(999, 31)

    assert actual is False
    db.rollback.assert_called_once()
    db.commit.assert_not_called()


def test_delete_user_returns_true_when_user_exists() -> None:
    db = Mock()

    result = Mock()
    result.scalar_one_or_none.return_value = 1
    db.execute.return_value = result

    repository = UserRepository(db)

    actual = repository.delete_user(1)

    assert actual is True
    db.commit.assert_called_once()
    db.rollback.assert_not_called()


def test_delete_user_returns_false_when_user_does_not_exist() -> None:
    db = Mock()

    result = Mock()
    result.scalar_one_or_none.return_value = None
    db.execute.return_value = result

    repository = UserRepository(db)

    actual = repository.delete_user(999)

    assert actual is False
    db.rollback.assert_called_once()
    db.commit.assert_not_called()
