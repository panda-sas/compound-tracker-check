# app/crud/batch.py

from sqlalchemy.orm import Session
from app.models import Batch
from app.schemas.batch import BatchCreate, BatchUpdate  # Assuming you have these schemas defined

# Create a new batch
def create_batch(db: Session, batch_data: BatchCreate):
    db_batch = Batch(**batch_data.model_dump(exclude_unset=True))
    db.add(db_batch)
    db.commit()
    db.refresh(db_batch)
    return db_batch

# Get a batch by ID
def get_batch(db: Session, batch_id: int):
    return db.query(Batch).filter(Batch.BatchId == batch_id).first()

# Update a batch by ID
def update_batch(db: Session, batch_id: int, batch_data: BatchUpdate):
    db_batch = db.query(Batch).filter(Batch.BatchId == batch_id).first()
    if db_batch:
        for key, value in batch_data.model_dump(exclude_unset=True).items():
            setattr(db_batch, key, value)
        db.commit()
        db.refresh(db_batch)
    return db_batch

# Delete a batch by ID
def delete_batch(db: Session, batch_id: int):
    db_batch = db.query(Batch).filter(Batch.BatchId == batch_id).first()
    if db_batch:
        db.delete(db_batch)
        db.commit()
    return db_batch
