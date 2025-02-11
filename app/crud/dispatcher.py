from sqlalchemy.orm import Session
from app.models.dispatcher import Dispatcher
from app.schemas.dispatcher import DispatcherCreate, DispatcherUpdate

def create_dispatcher(db: Session, dispatcher_data: DispatcherCreate):
    db_dispatcher = Dispatcher(**dispatcher_data.model_dump(exclude_unset=True))
    db.add(db_dispatcher)
    db.commit()
    db.refresh(db_dispatcher)
    return db_dispatcher

def get_all_dispatchers(db: Session):
    return db.query(Dispatcher).all()

def get_dispatcher(db: Session, dispatcher_id: int):
    return db.query(Dispatcher).filter(Dispatcher.DispatcherId == dispatcher_id).first()

def update_dispatcher(db: Session, dispatcher_id: int, dispatcher_data: DispatcherUpdate):
    db_dispatcher = db.query(Dispatcher).filter(Dispatcher.DispatcherId == dispatcher_id).first()
    if db_dispatcher:
        for key, value in dispatcher_data.model_dump(exclude_unset=True).items():
            setattr(db_dispatcher, key, value)
        db.commit()
        db.refresh(db_dispatcher)
    return db_dispatcher

def delete_dispatcher(db: Session, dispatcher_id: int):
    db_dispatcher = db.query(Dispatcher).filter(Dispatcher.DispatcherId == dispatcher_id).first()
    if db_dispatcher:
        db.delete(db_dispatcher)
        db.commit()
    return db_dispatcher
