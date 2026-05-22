from sqlalchemy.orm import Session
from app.books.models import Book
from app.watchlist.models import Watchlist

def create_book(db, user_id, data):
    book = Book(
        title=data.title.lower(),
        author=data.author,
        category=data.category,
        owner_id=user_id
    )
    db.add(book)
    db.commit()
    db.refresh(book)

    # 🔔 Match watchlist
    matches = db.query(Watchlist).filter(
        Watchlist.title == book.title,
        Watchlist.user_id != user_id
    ).all()

    for match in matches:
        print(f"Notify user {match.user_id} for book {book.title}")
    return book

def get_user_books(db: Session, user_id: int):
    return db.query(Book).filter(Book.owner_id == user_id).all()
