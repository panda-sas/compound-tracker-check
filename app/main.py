from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import create_order, get_order, update_order, delete_order  # Adjusted to the new path
from app.database import get_db  # Adjusted to the new path
from app.models import Order  # Adjusted to the new path

app = FastAPI()

@app.post("/orders/")
def create_order_endpoint(order_data: dict, db: Session = Depends(get_db)):
    return create_order(db=db, order_data=order_data)

@app.get("/orders/{order_id}")
def get_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    db_order = get_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.put("/orders/{order_id}")
def update_order_endpoint(order_id: int, order_data: dict, db: Session = Depends(get_db)):
    db_order = update_order(db, order_id, order_data)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.delete("/orders/{order_id}")
def delete_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    db_order = delete_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
