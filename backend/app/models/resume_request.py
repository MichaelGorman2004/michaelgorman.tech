from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.base import Base


class ResumeRequest(Base):
    __tablename__ = "resume_requests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, index=True)
    company = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
