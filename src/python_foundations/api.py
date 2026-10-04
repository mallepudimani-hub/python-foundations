from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.orm import Session

from python_foundations.database import get_db
from python_foundations.user_models import UserCreate, UserResponse
from python_foundations.user_service import (
    UserService,
    UserValidationError,
    get_user_service,
)

app = FastAPI()


def get_app_name() -> str:
    return "AI Engineering API"


@app.get("/hello")
def hello(name: str = "Mani") -> dict[str, str]:
    return {"message": f"Hello, {name}"}


@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, int]:
    return {"user_id": user_id}


@app.get("/users", response_model=list[UserResponse])
def get_users(
    user_service: UserService = Depends(get_user_service),
) -> list[UserResponse]:
    return user_service.get_users()


@app.post("/users", response_model=UserResponse)
def create_user(
    user: UserCreate,
    user_service: UserService = Depends(get_user_service),
) -> UserResponse:
    return user_service.create_user(user)


@app.exception_handler(UserValidationError)
def handle_user_validation_error(
    request: Request,
    error: UserValidationError,
) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": str(error)},
    )


@app.get("/app-info")
def app_info(app_name: str = Depends(get_app_name)) -> dict[str, str]:
    return {"app_name": app_name}


@app.get("/db-session")
def db_session(db: Session = Depends(get_db)) -> dict[str, str]:
    result = db.execute(text("SELECT current_database()"))
    database_name: str = result.scalar_one()

    return {"database": database_name}
