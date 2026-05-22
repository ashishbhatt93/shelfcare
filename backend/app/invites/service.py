import uuid
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.invites.models import Invite
from app.auth.models import User


INVITE_LIMIT_PER_MONTH = 2


def generate_invite_code():
    return str(uuid.uuid4())[:8]


def can_user_invite(user: User):
    if user.is_admin:
        return True

    # check cooling period
    if user.can_invite_after and user.can_invite_after > datetime.utcnow():
        return False

    # count invites this month
    start_of_month = datetime.utcnow().replace(day=1, hour=0, minute=0, second=0)

    count = db.query(Invite).filter(
        Invite.created_by == user.id,
        Invite.created_at >= start_of_month
    ).count()

    return count < INVITE_LIMIT_PER_MONTH

def create_invite(db: Session, user: User):

    now = datetime.utcnow()

    # Step 1: Check admin / cooling
    if not can_user_invite(user):
        raise Exception("Invite access locked (cooling period active)")

    # Step 2: Fetch active invites
    active_invites = db.query(Invite).filter(
        Invite.created_by == user.id,
        Invite.used_by == None,
        Invite.is_active == True,
        Invite.expires_at > now
    ).order_by(Invite.created_at.asc()).all()

    # Step 3: If already 2 active → invalidate them
    if len(active_invites) >= 2:
        for inv in active_invites:
            inv.is_active = False
            inv.expires_at = now
        db.commit()

    # Step 4: Create new invite (24h)
    invite = Invite(
        code=str(uuid.uuid4())[:8],
        created_by=user.id,
        expires_at=now + timedelta(hours=24)
    )

    db.add(invite)
    db.commit()
    db.refresh(invite)

    return invite
