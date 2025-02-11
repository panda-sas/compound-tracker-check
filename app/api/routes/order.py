from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.order import get_order  # Correct import
from app.database import get_db

router = APIRouter()

@router.get("/order-details/{order_id}")
def order_details(order_id: int, db: Session = Depends(get_db)):
    order = get_order(db, order_id)  # Call get_order directly
    if order:
        return order
    raise HTTPException(status_code=404, detail="Order not found")
