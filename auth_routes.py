from fastapi import APIRouter, HTTPException, status

from database import session
from schemas import SignUpModel
from models import User

auth_router = APIRouter(
    prefix="/auth",
)


@auth_router.get("/")
async def sing_up_user():
    return {"message": "This page auth"}


@auth_router.post("/signup ")
async def signup(user: SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()
    if db_email is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")

    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        is_active=user.is_active,
        is_staff=user.is_staff,
    )
