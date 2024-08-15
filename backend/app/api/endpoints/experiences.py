from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Experience])
def read_experiences(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
):
    experiences = crud.experience.get_multi(db, skip=skip, limit=limit)
    return experiences


@router.post("/", response_model=schemas.Experience)
def create_experience(
    *,
    db: Session = Depends(deps.get_db),
    experience_in: schemas.ExperienceCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    experience = crud.experience.create(db, obj_in=experience_in)
    return experience


@router.put("/{id}", response_model=schemas.Experience)
def update_experience(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    experience_in: schemas.ExperienceUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    experience = crud.experience.get(db, id=id)
    if not experience:
        raise HTTPException(status_code=404, detail="Experience not found")
    experience = crud.experience.update(db, db_obj=experience, obj_in=experience_in)
    return experience


@router.get("/{id}", response_model=schemas.Experience)
def read_experience(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
):
    experience = crud.experience.get(db, id=id)
    if not experience:
        raise HTTPException(status_code=404, detail="Experience not found")
    return experience


@router.delete("/{id}", response_model=schemas.Experience)
def delete_experience(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
):
    experience = crud.experience.get(db, id=id)
    if not experience:
        raise HTTPException(status_code=404, detail="Experience not found")
    experience = crud.experience.remove(db, id=id)
    return experience
