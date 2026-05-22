from fastapi import APIRouter, Depends, Header, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.books.schemas import BookCreate, BookResponse
from app.books.service import create_book, get_user_books
from app.models import User, Book
from app.invites.routes import get_current_user
from typing import List

router = APIRouter(prefix="/books", tags=["Books"])
VALID_CATEGORIES = ["lend", "sell"]

# TEMP: reuse mock user

def get_current_user(
    x_user_id: int = Header(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.id == x_user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.post("/", response_model=BookResponse)
def add_book(data: BookCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_book(db, user.id, data)


@router.get("/", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_user_books(db, user.id)

@router.get("/marketplace", response_model=List[BookResponse])
def get_marketplace(
    category: str = None,
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    query = db.query(Book).filter(Book.owner_id != user.id)

    if category:
        if category not in VALID_CATEGORIES:
            raise HTTPException(status_code=400, detail="Invalid category")
        query = query.filter(Book.category == category)

    query = query.order_by(Book.id.desc())

    return query.offset(offset).limit(limit).all()
