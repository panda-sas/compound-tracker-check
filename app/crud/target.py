from sqlalchemy.orm import Session
from app.models.target import Target
from app.schemas.target import TargetCreate, TargetUpdate

def create_target(db: Session, target_data: TargetCreate):
    db_target = Target(**target_data.model_dump(exclude_unset=True))
    db.add(db_target)
    db.commit()
    db.refresh(db_target)
    return db_target

def get_target(db: Session, target_id: int):
    return db.query(Target).filter(Target.TargetID == target_id).first()

def update_target(db: Session, target_id: int, target_data: TargetUpdate):
    db_target = db.query(Target).filter(Target.TargetID == target_id).first()
    if db_target:
        for key, value in target_data.model_dump(exclude_unset=True).items():
            setattr(db_target, key, value)
        db.commit()
        db.refresh(db_target)
    return db_target

def delete_target(db: Session, target_id: int):
    db_target = db.query(Target).filter(Target.TargetID == target_id).first()
    if db_target:
        db.delete(db_target)
        db.commit()
    return db_target
