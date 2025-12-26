from fastapi import FastAPI
from fastapi_jwt_auth import AuthJWT

from auth_routes import auth_router
from order_routes import order_router
from database import engine
from models import Base
from schemas import Settings, LoginModel

app = FastAPI()


# DB da table create bo'lmagan bo'lsa create qiladi
# @app.on_event("startup")
# def startup():
#     Base.metadata.create_all(bind=engine)




@AuthJWT.load_config
def get_config():
    return Settings()



app.include_router(auth_router)
app.include_router(order_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
