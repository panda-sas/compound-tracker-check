from sqlalchemy.orm import Session
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate

def create_order(db: Session, order_data: OrderCreate):
    db_order = Order(**order_data.model_dump(exclude_unset=True))  # Convert Pydantic model to dict (old way, could be deprecated)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_all_orders(db: Session):
    return db.query(Order).all()

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.OrderID == order_id).first()

def update_order(db: Session, order_id: int, order_data: OrderUpdate):
    db_order = db.query(Order).filter(Order.OrderID == order_id).first()
    if db_order:
        # Only update fields that are provided (using model_dump or dict(exclude_unset=True) to avoid the deprecation)
        for key, value in order_data.model_dump(exclude_unset=True).items():  # Using dict with exclude_unset=True
            setattr(db_order, key, value)
        db.commit()
        db.refresh(db_order)
        return db_order
    return None  # Explicitly return None if not found

def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.OrderID == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
        return db_order
    return None  # Explicitly return None if not found
