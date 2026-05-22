from app.watchlist.models import Watchlist

def add_to_watchlist(db, user_id, data):
    watch = Watchlist(
        user_id=user_id,
        title=data.title.lower()
    )
    db.add(watch)
    db.commit()
    db.refresh(watch)
    return watch


def get_watchlist(db, user_id):
    return db.query(Watchlist).filter(Watchlist.user_id == user_id).all()
