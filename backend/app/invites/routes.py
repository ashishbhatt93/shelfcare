from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.auth.models import User
from app.invites.service import create_invite
from app.books.schemas import BookCreate, BookResponse
from app.books.service import create_book, get_user_books

router = APIRouter(prefix="/invites", tags=["Invites"])

# TEMP: mock user (we'll replace with JWT laterer(db: Session = Depends(get_db)):
def get_current_user(db: Session = Depends(get_db)):
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="No users found")
    return user


@router.post("/")
def generate_invite(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    try:
        invite = create_invite(db, user)
        return {"invite_code": invite.code}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
