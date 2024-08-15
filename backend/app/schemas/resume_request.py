from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class ResumeRequestBase(BaseModel):
    name: str
    email: EmailStr
    company: Optional[str] = None


class ResumeRequestCreate(ResumeRequestBase):
    pass


class ResumeRequestInDBBase(ResumeRequestBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ResumeRequest(ResumeRequestInDBBase):
    pass
