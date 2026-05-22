from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from app.auth.schemas import RegisterRequest
from app.auth.models import User
from app.invites.models import Invite


def register_user(db: Session, data: RegisterRequest):

    # check if user already exists
    existing_user = db.query(User).filter(User.phone_number == data.phone_number).first()
    if existing_user:
        raise Exception("User already exists")

    existing_email = db.query(User).filter(User.email == data.email).first()
    if existing_email:
            raise Exception("Email already registered")

    # validate invite
    #invite = db.query(Invite).filter(Invite.code == invite_code).first()
    invite = db.query(Invite).filter(Invite.code == data.invite_code).first()

    if not invite:
        raise Exception("Invalid invite code")

    if invite.used_by:
        raise Exception("Invite already used")

    if invite.expires_at and invite.expires_at < datetime.utcnow():
        raise Exception("Invite expired")


    pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto"
    )
    hashed_password = pwd_context.hash(data.password)

    # create user
    new_user = User(
        name=data.name,
        email=data.email,
        phone_number=data.phone_number,
        password_hash=hashed_password,
        invited_by=invite.created_by,
        can_invite_after=datetime.utcnow() + timedelta(days=7)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # mark invite as used
    invite.used_by = new_user.id
    invite.is_active = False
    db.commit()

    return new_user
