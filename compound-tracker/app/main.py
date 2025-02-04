from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud.order import create_order, get_order, update_order, delete_order  # Adjusted to the new path
from app.crud.batch import create_batch, get_batch, update_batch, delete_batch
from app.crud.compound import create_compound, get_compound, update_compound, delete_compound

from app.database import get_db  # Adjusted to the new path
from app.models.order import Order  # Adjusted to the new path

app = FastAPI()

#Order Routes

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

# Batch Routes
@app.post("/batches/")
def create_batch_endpoint(batch_data: dict, db: Session = Depends(get_db)):
    return create_batch(db=db, batch_data=batch_data)

@app.get("/batches/{batch_id}")
def get_batch_endpoint(batch_id: int, db: Session = Depends(get_db)):
    db_batch = get_batch(db, batch_id)
    if db_batch is None:
        raise HTTPException(status_code=404, detail="Batch not found")
    return db_batch

@app.put("/batches/{batch_id}")
def update_batch_endpoint(batch_id: int, batch_data: dict, db: Session = Depends(get_db)):
    db_batch = update_batch(db, batch_id, batch_data)
    if db_batch is None:
        raise HTTPException(status_code=404, detail="Batch not found")
    return db_batch

@app.delete("/batches/{batch_id}")
def delete_batch_endpoint(batch_id: int, db: Session = Depends(get_db)):
    db_batch = delete_batch(db, batch_id)
    if db_batch is None:
        raise HTTPException(status_code=404, detail="Batch not found")
    return db_batch

# Compound Routes
@app.post("/compounds/")
def create_compound_endpoint(compound_data: dict, db: Session = Depends(get_db)):
    return create_compound(db=db, compound_data=compound_data)

@app.get("/compounds/{compound_id}")
def get_compound_endpoint(compound_id: int, db: Session = Depends(get_db)):
    db_compound = get_compound(db, compound_id)
    if db_compound is None:
        raise HTTPException(status_code=404, detail="Compound not found")
    return db_compound

@app.put("/compounds/{compound_id}")
def update_compound_endpoint(compound_id: int, compound_data: dict, db: Session = Depends(get_db)):
    db_compound = update_compound(db, compound_id, compound_data)
    if db_compound is None:
        raise HTTPException(status_code=404, detail="Compound not found")
    return db_compound

@app.delete("/compounds/{compound_id}")
def delete_compound_endpoint(compound_id: int, db: Session = Depends(get_db)):
    db_compound = delete_compound(db, compound_id)
    if db_compound is None:
        raise HTTPException(status_code=404, detail="Compound not found")
    return db_compound
