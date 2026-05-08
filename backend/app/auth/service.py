from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models import Invite, User


def register_user(db: Session, phone: str, invite_code: str):

    # check if user already exists
    existing_user = db.query(User).filter(User.phone_number == phone).first()
    if existing_user:
        raise Exception("User already exists")

    # validate invite
    invite = db.query(Invite).filter(Invite.code == invite_code).first()

    if not invite:
        raise Exception("Invalid invite code")

    if invite.used_by:
        raise Exception("Invite already used")

    if invite.expires_at and invite.expires_at < datetime.utcnow():
        raise Exception("Invite expired")

    # create user
    new_user = User(
        phone_number=phone,
        invited_by=invite.created_by,
        can_invite_after=datetime.utcnow() + timedelta(days=7)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # mark invite as used
    invite.used_by = new_user.id
    db.commit()

    return new_user
