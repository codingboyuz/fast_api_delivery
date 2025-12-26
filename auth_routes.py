from http.client import responses

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder

from database import session, engine
from schemas import SignUpModel, LoginModel
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from fastapi_jwt_auth import AuthJWT

auth_router = APIRouter(
    prefix="/auth",
)

session = session(bind=engine)


@auth_router.get("/login")
async def signup_user():
    return {"message": "Welcome to FastAPI!"}


@auth_router.post("/login", status_code=status.HTTP_200_OK)
async def login(user: LoginModel, Authorize: AuthJWT = Depends()):
    db_username = session.query(User).filter(User.username == user.username).first()

    # db_username dbga saqlangan user bo'lib check_password_hash fuksiyasi orqali parol tekshirib olinadi
    if db_username and check_password_hash(db_username.password, user.password):
        # Token ni yaratamiz va responseda yuboramiz
        access_token = Authorize.create_access_token(subject=db_username.username)
        refresh_token = Authorize.create_refresh_token(subject=db_username.username)

        response_data = {
            'access_token': access_token,
            'refresh_token': refresh_token,

        }
        # dict malumotni json ko'rinishiga aylantiradi ```jsonable_encoder``` fastapi da default mavjud
        return jsonable_encoder(response_data)
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")


@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: SignUpModel):
    db_email = session.query(User).filter(User.email == user.email).first()

    if db_email is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    db_username = session.query(User).filter(User.username == user.username).first()
    if db_username is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")

    new_user = User(
        username=user.username,
        email=user.email,
        password=generate_password_hash(user.password),
        is_active=user.is_active,
        is_staff=user.is_staff,
    )

    session.add(new_user)
    session.commit()
    data = {
        'id': new_user.id,
        'username': new_user.username,
        'email': new_user.email,
        'is_active': new_user.is_active,
        'is_staff': new_user.is_staff,
    }

    response_data = {
        'success': True,
        'data': data,
        'message': 'User created successfully',
    }

    return response_data
