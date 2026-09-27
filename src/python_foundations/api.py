from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserCreate(BaseModel):
    name: str
    email: str
    age: int


class UserResponse(BaseModel):
    name: str
    email: str
    age: int


@app.get("/hello")
def hello(name: str = "Mani") -> dict[str, str]:
    return {"message": f"Hello, {name}"}


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, int]:
    return {"user_id": user_id}


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate) -> UserResponse:
    return UserResponse(
        name=user.name,
        email=user.email,
        age=user.age,
    )
