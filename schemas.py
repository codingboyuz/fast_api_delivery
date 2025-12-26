from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff:Optional[bool]
    is_active:Optional[bool]


    class Config:
        orm_mode = True
        schema_extra ={
            "example" :
                {
                    'username': 'admin',
                    'email': 'test@gmail.com',
                    'password': "test1234",
                    'is_staff':False,
                    'is_active':True
                }
        }


class Settings(BaseModel):
    authjwt_secret_key: str  = "a57a608cfaa0697145650bf70ef4ddeed75196d2a620d63fdd539fbb636608a1"



class LoginModel(BaseModel):
    username: str
    password: str
