from sqlalchemy import Column, Integer, String, Text
from app.db.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    github_link = Column(String)
    live_link = Column(String)
