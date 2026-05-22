from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.db import get_db
from app.auth.models import User
from app.watchlist.schemas import WatchCreate, WatchResponse
from app.watchlist.service import add_to_watchlist, get_watchlist
from app.invites.routes import get_current_user

router = APIRouter(prefix="/watchlist", tags=["Watchlist"])


@router.post("/", response_model=WatchResponse)
def add_watch(
    data: WatchCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return add_to_watchlist(db, user.id, data)


@router.get("/", response_model=List[WatchResponse])
def list_watch(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    return get_watchlist(db, user.id)
