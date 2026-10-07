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
