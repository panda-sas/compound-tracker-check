# app/crud/compound.py

from sqlalchemy.orm import Session
from app.models import Compound
from app.schemas.compound import CompoundCreate, CompoundUpdate  # Assuming you have these schemas defined

# Create a new compound
def create_compound(db: Session, compound_data: CompoundCreate):
    db_compound = Compound(**compound_data.model_dump(exclude_unset=True))
    db.add(db_compound)
    db.commit()
    db.refresh(db_compound)
    return db_compound

# Get a compound by ID
def get_compound(db: Session, compound_id: int):
    return db.query(Compound).filter(Compound.CompoundId == compound_id).first()

# Update a compound by ID
def update_compound(db: Session, compound_id: int, compound_data: CompoundUpdate):
    db_compound = db.query(Compound).filter(Compound.CompoundId == compound_id).first()
    if db_compound:
        for key, value in compound_data.model_dump(exclude_unset=True).items():
            setattr(db_compound, key, value)
        db.commit()
        db.refresh(db_compound)
    return db_compound

# Delete a compound by ID
def delete_compound(db: Session, compound_id: int):
    db_compound = db.query(Compound).filter(Compound.CompoundId == compound_id).first()
    if db_compound:
        db.delete(db_compound)
        db.commit()
    return db_compound
