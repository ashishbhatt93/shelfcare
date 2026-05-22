from fastapi import FastAPI
from app.db import engine, Base
from app.invites.routes import router as invite_router
from app.auth.routes import router as auth_router
from app.books.routes import router as books_router
from app.watchlist.routes import router as watchlist_router
from app.ocr.routes import router as ocr_router
from app.auth.models import User
from app.invites.models import Invite
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Book Marketplace API")
app.add_middleware(
    CORSMiddleware,
#    allow_origins=["*"],
    allow_origin_regex=r"http://.*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables on startup (for MVP)
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

@app.get("/health")
def health_check():
    return {"status": "ok"}
app.include_router(invite_router)
app.include_router(auth_router)
app.include_router(books_router)
app.include_router(watchlist_router)
app.include_router(ocr_router)
