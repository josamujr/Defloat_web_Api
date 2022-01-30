from fastapi import APIRouter, Depends, status, HTTPException, Response
import schemas, authentication2, models, main
from sqlalchemy.orm import Session

router = APIRouter(prefix="/vote", tags=["Vote"])

@router.post("/", status_code= status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(main.get_database), current_user : int = Depends(authentication2.get_current_user)):
    check_post_existence = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not check_post_existence:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Post with id {vote.post_id} was not found")

    vote_query = db.query(models.Votes).filter(models.Votes.post_id == vote.post_id,models.Votes.user_id == current_user.id)
    found_vote = vote_query.first()
    if vote.dir == 1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f"User {current_user.id} has already voted for {vote.post_id}")
        new_vote = models.Votes(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()

        return {"DONE": "A post has been voted successfully"}

    else:
        if not found_vote:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "A vote was not found")
        vote_query.delete(synchronize_session = False)
        db.commit()

        return {"DONE" : "A vote has been deleted succcessfully"}