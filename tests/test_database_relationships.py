from sqlalchemy import select
from sqlalchemy.orm import selectinload

from python_foundations.database import SessionLocal
from python_foundations.db_models import Address, User


def test_user_address_relationship() -> None:
    db = SessionLocal()

    try:
        user = User(
            name="Relationship Test",
            email="relationship@example.com",
            age=30,
        )

        address = Address(
            street="123 Main Street",
            city="Hyderabad",
        )

        user.addresses.append(address)

        db.add(user)
        db.commit()
        db.refresh(user)

        assert address.user is user
        assert user.addresses[0] is address

    finally:
        db.query(Address).filter(Address.user_id == user.id).delete()
        db.query(User).filter(User.id == user.id).delete()
        db.commit()
        db.close()


def test_delete_user_deletes_addresses() -> None:
    db = SessionLocal()

    try:
        user = User(
            name="Cascade Test",
            email="cascade@example.com",
            age=30,
        )

        address = Address(
            street="456 Test Street",
            city="Hyderabad",
        )

        user.addresses.append(address)

        db.add(user)
        db.commit()

        user_id = user.id
        address_id = address.id

        db.delete(user)
        db.commit()

        assert db.get(User, user_id) is None
        assert db.get(Address, address_id) is None

    finally:
        db.rollback()
        db.close()

    def test_get_users_with_addresses() -> None:
        db = SessionLocal()

        try:
            user = User(
                name="Loading Test",
                email="loading@example.com",
                age=30,
            )

            address = Address(
                street="789 Loading Street",
                city="Hyderabad",
            )

            user.addresses.append(address)

            db.add(user)
            db.commit()

            statement = (
                select(User)
                .options(selectinload(User.addresses))
                .where(User.id == user.id)
            )

            result = db.execute(statement)
            loaded_user = result.scalar_one()

            assert len(loaded_user.addresses) == 1
            assert loaded_user.addresses[0].city == "Hyderabad"

        finally:
            db.rollback()
            db.close()
