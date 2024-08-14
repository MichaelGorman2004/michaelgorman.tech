from pydantic import BaseModel
from datetime import date
from typing import Optional


class ExperienceBase(BaseModel):
    title: str
    company: str
    location: str
    start_date: date
    end_date: Optional[date] = None
    description: str


class ExperienceCreate(ExperienceBase):
    pass


class ExperienceUpdate(ExperienceBase):
    pass


class ExperienceInDBBase(ExperienceBase):
    id: int

    class Config:
        orm_mode = True


class Experience(ExperienceInDBBase):
    pass
