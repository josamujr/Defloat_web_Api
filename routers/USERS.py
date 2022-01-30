import models, schemas, UTILITIES
from fastapi import FastAPI, Depends, status, HTTPException, APIRouter
from fastapi.params import Body
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from home import get_database


router= APIRouter()


@router.post("/users", status_code= status.HTTP_201_CREATED, response_model= schemas.user_output)
def new_user(user : schemas.validate_user ,db :Session = Depends(get_database)):

    #hashi the password
    hashed_password = UTILITIES.HASH(user.password)
    user.password = hashed_password

    new_user = models.User(email=user.email, password=user.password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/users/{id}', response_model=schemas.user_output)
def get_user(id: int, db :Session = Depends(get_database)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No user was found with id {id}')
    return user



@router.get("/get_users")
def get_all_users(db :Session = Depends(get_database)):
    data = db.query(models.User).all()
    return data
