from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from python_foundations.user_models import UserCreate, UserResponse
from python_foundations.user_service import UserValidationError
from python_foundations.user_service import create_user as create_user_service

app = FastAPI()


@app.get("/hello")
def hello(name: str = "Mani") -> dict[str, str]:
    return {"message": f"Hello, {name}"}


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, int]:
    return {"user_id": user_id}


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate) -> UserResponse:
    return create_user_service(user)


@app.exception_handler(UserValidationError)
def handle_user_validation_error(
    request: Request,
    error: UserValidationError,
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": str(error)},
    )
