from sqlalchemy import Column, Integer, String, Text, Date
from app.db.base import Base


class Experience(Base):
    __tablename__ = "experiences"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String)
    location = Column(String)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    description = Column(Text)
