from sqlalchemy.orm import Session
from app.models.checkinout import CheckInOut
from app.schemas.checkinout import CheckInOutCreate, CheckInOutUpdate

def create_checkinout(db: Session, checkinout_data: CheckInOutCreate):
    db_checkinout = CheckInOut(**checkinout_data.model_dump(exclude_unset=True))
    db.add(db_checkinout)
    db.commit()
    db.refresh(db_checkinout)
    return db_checkinout

def get_checkinout(db: Session, checkinout_id: int):
    return db.query(CheckInOut).filter(CheckInOut.CheckOutId == checkinout_id).first()

def update_checkinout(db: Session, checkinout_id: int, checkinout_data: CheckInOutUpdate):
    db_checkinout = db.query(CheckInOut).filter(CheckInOut.CheckOutId == checkinout_id).first()
    if db_checkinout:
        for key, value in checkinout_data.model_dump(exclude_unset=True).items():
            setattr(db_checkinout, key, value)
        db.commit()
        db.refresh(db_checkinout)
    return db_checkinout

def delete_checkinout(db: Session, checkinout_id: int):
    db_checkinout = db.query(CheckInOut).filter(CheckInOut.CheckOutId == checkinout_id).first()
    if db_checkinout:
        db.delete(db_checkinout)
        db.commit()
    return db_checkinout
