import pytest
from fastapi.testclient import TestClient

from python_foundations.api import app
from python_foundations.user_models import UserCreate, UserResponse
from python_foundations.user_service import get_user_service


class FakeUserService:
    def create_user(self, user: UserCreate) -> UserResponse:
        return UserResponse(
            name="Fake User",
            email="fake@example.com",
            age=30,
        )

    def get_user_by_id(self, user_id: int) -> UserResponse | None:
        if user_id == 1:
            return UserResponse(
                name="Fake User",
                email="fake@example.com",
                age=30,
            )

        return None


@pytest.fixture
def fake_user_service() -> None:
    app.dependency_overrides[get_user_service] = lambda: FakeUserService()

    yield

    app.dependency_overrides.clear()


client = TestClient(app)


def test_create_user_uses_fake_service(
    fake_user_service: None,
) -> None:
    response = client.post(
        "/users",
        json={
            "name": "Mani",
            "email": "mani@example.com",
            "age": 30,
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "name": "Fake User",
        "email": "fake@example.com",
        "age": 30,
    }


def test_get_user_returns_user(
    fake_user_service: None,
) -> None:
    response = client.get("/users/1")

    assert response.status_code == 200
    assert response.json() == {
        "name": "Fake User",
        "email": "fake@example.com",
        "age": 30,
    }


def test_get_user_returns_404_when_user_not_found(
    fake_user_service: None,
) -> None:
    response = client.get("/users/999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "User not found",
    }
