from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Index
from sqlalchemy.sql import func
from app.db import Base

class Invite(Base):
    __tablename__ = "invites"

    id = Column(Integer, primary_key=True, index=True)

    code = Column(String(20), unique=True, nullable=False)

    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    used_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    expires_at = Column(DateTime, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)

    __table_args__ = (
        Index("idx_invites_created_by", "created_by"),
        Index("idx_invites_used_by", "used_by"),
    )
