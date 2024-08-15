from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.ResumeRequest)
def create_resume_request(
    *,
    db: Session = Depends(deps.get_db),
    resume_request_in: schemas.ResumeRequestCreate,
):
    resume_request = crud.resume_request.create(db, obj_in=resume_request_in)
    return resume_request


@router.get("/", response_model=List[schemas.ResumeRequest])
def read_resume_requests(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    resume_requests = crud.resume_request.get_multi(db, skip=skip, limit=limit)
    return resume_requests


@router.get("/{id}", response_model=schemas.ResumeRequest)
def read_resume_request(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
):
    resume_request = crud.resume_request.get(db, id=id)
    if not resume_request:
        raise HTTPException(status_code=404, detail="Resume request not found")
    return resume_request
