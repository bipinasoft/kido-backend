from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas

router = APIRouter(prefix="/progress", tags=["Progress"])

@router.post("/", response_model=schemas.Progress)
def create_progress(progress: schemas.ProgressCreate, db: Session = Depends(get_db)):
    new_progress = models.Progress(**progress.dict())
    db.add(new_progress)
    db.commit()
    db.refresh(new_progress)
    return new_progress

@router.get("/", response_model=list[schemas.Progress])
def list_progress(db: Session = Depends(get_db)):
    return db.query(models.Progress).all()

@router.get("/{progress_id}", response_model=schemas.Progress)
def get_progress(progress_id: int, db: Session = Depends(get_db)):
    progress = db.query(models.Progress).filter(models.Progress.id == progress_id).first()
    if not progress:
        raise HTTPException(status_code=404, detail="Progress not found")
    return progress
