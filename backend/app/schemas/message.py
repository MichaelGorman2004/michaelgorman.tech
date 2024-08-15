from pydantic import BaseModel, EmailStr
from datetime import datetime


class MessageBase(BaseModel):
    name: str
    email: EmailStr
    subject: str
    content: str


class MessageCreate(MessageBase):
    pass


class MessageInDBBase(MessageBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class Message(MessageInDBBase):
    pass
