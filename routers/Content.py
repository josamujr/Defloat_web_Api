import models, schemas, UTILITIES, authentication2
from fastapi import FastAPI, Depends, status, HTTPException, APIRouter
from fastapi.params import Body
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from home import get_database
from typing import List, Optional
from sqlalchemy import func

router = APIRouter()
@router.get("/sqlalchemy", response_model= schemas.Response)
def list_all(db :Session = Depends(get_database), get_user: int = Depends(authentication2.get_current_user)):
    data = db.query(models.Post).all()
    return data
@router.get("/getdata", response_model=List[schemas.PostResponse])
def test(db :Session = Depends(get_database), limit : int = 10, skip : int = 0, search : Optional[str] = ""):
    data = db.query(models.Post).all()

    results = db.query(models.Post, func.count(models.Votes.post_id).label("votes")).join(models.Votes, models.Votes.post_id == models.Post.id, isouter=True).group_by(models.Post.id).\
        filter( models.Post.title.contains(search)).limit(limit).offset(skip).all()

    return results
@router.get("/userdata")
def list_based_on_user(db :Session = Depends(get_database), get_user: int = Depends(authentication2.get_current_user)):
    data = db.query(models.Post).filter(models.Post.user_id == get_user.id).all()
    return {"Connection result": data}

@router.post("/new_data", response_model= schemas.Response)
def first_post(rec: schemas.insert_new,db :Session = Depends(get_database), get_user: int = Depends(authentication2.get_current_user)):
    print(get_user.id)
    insert_data = models.Post( title = rec.title, content = rec.content, user_id =get_user.id)

    db.add(insert_data)
    db.commit()
    db.refresh(insert_data)
    return insert_data
@router.get("/select_byId/{id}", response_model= schemas.Response)
def get_by_id(id : int, db :Session = Depends(get_database), get_user: int = Depends(authentication2.get_current_user)):
    data = db.query(models.Post).filter(models.Post.id == id).first()

    if not data:
        pass
    return data


@router.delete("/delete/{id}")
def delete(id : int, db :Session = Depends(get_database), get_user: int = Depends(authentication2.get_current_user)):
    del_item = db.query(models.Post).filter(models.Post.id == id)
    post = del_item.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The item you are trying to delete was not found in the database')
    if post.user_id != get_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail='You can not delete this because it was not created by you')
    del_item.delete(synchronize_session = False)
    db.commit()
    return {'Info': 'A record has been deleted successfully'}

@router.put("/update/{id}", status_code= status.HTTP_404_NOT_FOUND)
def update_records(id : int, db :Session = Depends(get_database), get_user: int = Depends(authentication2.get_current_user)):
    recoord = db.query(models.Post).filter(models.Post.id == id)

    Record = recoord.first()
    if recoord.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='The item you are trying to delete was not found in the database')

    if Record.user_id != get_user.id:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail='You can not update this because it was not created by you')

    recoord.update({'title': "Tasintha title yokha"},synchronize_session = False)
    db.commit()

    return{'Result': 'A record has been updated successfully'}
