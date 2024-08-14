from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Message)
def create_message(
    *,
    db: Session = Depends(deps.get_db),
    message_in: schemas.MessageCreate,
):
    message = crud.message.create(db, obj_in=message_in)
    return message


@router.get("/", response_model=List[schemas.Message])
def read_messages(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    messages = crud.message.get_multi(db, skip=skip, limit=limit)
    return messages


@router.get("/{id}", response_model=schemas.Message)
def read_message(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
):
    message = crud.message.get(db, id=id)
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message
