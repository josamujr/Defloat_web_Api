from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
import main, schemas, models, UTILITIES as utils, authentication2

router = APIRouter(tags=['Authentication'])

@router.post("/login", response_model= schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db : Session = Depends(main.get_database) ):
    user_logged_in = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user_logged_in:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='INVALID CREDENTIALS')

    has = utils.get_password_hash(user_logged_in.password)

    if not utils.verify_password(user_credentials.password, has):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='INVALID CREDENTIALS')
    # create a token

    access_token = authentication2.create_token(data={ "user_id": user_logged_in.id})
    print(access_token)
    # return token
    return {"access_token": access_token, "token_type": "Bearer"}
