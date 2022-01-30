from jose import jwt, JWTError
from datetime import datetime, timedelta
import schemas, main, models
from  fastapi import Depends, status , HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from config import settings

oath2_scheme = OAuth2PasswordBearer(tokenUrl='login')
secrete_key = settings.secrete_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_token(data : dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    print(expire)
    to_encode.update({"exp" :expire})

    encoded_jwt = jwt.encode(to_encode, secrete_key, algorithm= ALGORITHM)

    return encoded_jwt

def verify_access_token(token : str, credentials_exception):
    try:
        payload = jwt.decode(token, secrete_key, algorithms= ALGORITHM)

        id : str = payload.get("user_id")
        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id = id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token : str = Depends(oath2_scheme), dbc :Session = Depends(main.get_database)):
    credential_exceptopn = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail='UN AUTHORISED ACESS', headers={"WWW--AUTHENTICATE" : "Bearer"})
    TOKEN = verify_access_token(token, credential_exceptopn)
    user = dbc.query(models.User).filter(models.User.id == TOKEN.id).first()
    return user

