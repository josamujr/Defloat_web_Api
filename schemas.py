from pydantic import BaseModel, EmailStr
from typing import Optional
from pydantic.types import conint



class authenticate(BaseModel):
    title : str
    content : str

class insert_new(authenticate):
    pass
class user_output(BaseModel):
    email: EmailStr
    id : int
    #password : str
    class Config:
        orm_mode = True


class Response(BaseModel):
    title: str
    content: str
    user_id : int
    owner : user_output
    class Config:
        orm_mode = True

class validate_user(BaseModel):
    email : EmailStr
    password : str



class Userlogin(BaseModel):
    email : EmailStr
    password : str


class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id : int
    dir : conint(le=1)

class PostResponse(BaseModel):
    Post : Response
    votes : int

    class COnfig:
        orm_mode = True
