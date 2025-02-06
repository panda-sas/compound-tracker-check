from sqlalchemy.orm import Session
from app.models.scientist import Scientist
from app.schemas.scientist import ScientistCreate, ScientistUpdate

def create_scientist(db: Session, scientist_data: ScientistCreate):
    db_scientist = Scientist(**scientist_data.model_dump(exclude_unset=True))
    db.add(db_scientist)
    db.commit()
    db.refresh(db_scientist)
    return db_scientist

def get_scientist(db: Session, scientist_id: int):
    return db.query(Scientist).filter(Scientist.ScientistID == scientist_id).first()

def update_scientist(db: Session, scientist_id: int, scientist_data: ScientistUpdate):
    db_scientist = db.query(Scientist).filter(Scientist.ScientistID == scientist_id).first()
    if db_scientist:
        for key, value in scientist_data.model_dump(exclude_unset=True).items():
            setattr(db_scientist, key, value)
        db.commit()
        db.refresh(db_scientist)
    return db_scientist

def delete_scientist(db: Session, scientist_id: int):
    db_scientist = db.query(Scientist).filter(Scientist.ScientistID == scientist_id).first()
    if db_scientist:
        db.delete(db_scientist)
        db.commit()
    return db_scientist

def get_all_scientists(db: Session):
    return db.query(Scientist).all()

