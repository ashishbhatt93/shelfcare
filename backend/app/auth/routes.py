from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.auth.schemas import RegisterRequest
from app.auth.schemas import LoginRequest
from app.auth.service import register_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup")
def signup(data: RegisterRequest, db: Session = Depends(get_db)):
    try:
        user = register_user(db, data)
        return {
            "message": "User registered successfully",
            "user_id": user.id
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(
    data: LoginRequest,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.phone_number == data.phone_number
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "Login successful",
        "user_id": user.id
    }
