from fastapi import APIRouter



auth_router = APIRouter(
    prefix="/auth",
)

@auth_router.get("/")
async def sing_up_user():
    return {"message": "This page auth"}
