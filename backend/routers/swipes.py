from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.swipe import SwipeCreate, SwipeResponse
from database import get_db
from auth import get_current_user
from models.swipe import Swipe

router = APIRouter(prefix="/swipes")

@router.post('', response_model=SwipeResponse, status_code=201)
def create_swipe(swipe: SwipeCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user),):
    existing_swipe = db.query(Swipe).filter(
    Swipe.user_id == current_user.id,
    Swipe.job_id == swipe.job_id).first()


    if existing_swipe:
        db.delete(existing_swipe)
        db.commit()

    new_swipe = Swipe(
        user_id = current_user.id,
        job_id = swipe.job_id,
        action = swipe.action
    )

    db.add(new_swipe)
    db.commit()
    db.refresh(new_swipe)

    return new_swipe
        