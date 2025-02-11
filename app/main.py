from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.api.routes import order
from app.crud.order import create_order, get_order, update_order, delete_order, get_all_orders  # Adjusted to the new path
from app.crud.batch import create_batch, get_batch, update_batch, delete_batch
from app.crud.compound import create_compound, get_compound, update_compound, delete_compound
from app.crud.scientist import create_scientist, get_scientist, update_scientist, delete_scientist, get_all_scientists
from app.schemas.scientist import ScientistCreate, ScientistUpdate
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.schemas.target import TargetCreate, TargetUpdate
from app.schemas.order import OrderCreate, OrderUpdate
from app.schemas.batch import BatchCreate, BatchUpdate
from app.schemas.compound import CompoundCreate, CompoundUpdate
from app.schemas.dispatcher import DispatcherCreate, DispatcherUpdate
from app.schemas.checkinout import CheckInOutCreate, CheckInOutUpdate
from app.crud.dispatcher import create_dispatcher, get_dispatcher, update_dispatcher, delete_dispatcher
from app.crud.project import create_project, get_project, update_project, delete_project, get_all_projects
from app.crud.target import create_target, get_target, update_target, delete_target
from app.crud.checkinout import create_checkinout, get_checkinout, update_checkinout, delete_checkinout


from app.database import get_db  # Adjusted to the new path

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],  # Allow your frontend's URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Include the order router
app.include_router(order.router)

#Order Routes
@app.get("/order-details/")
def get_orders(db: Session = Depends(get_db)):
    return get_all_orders(db)

@app.post("/orders/")
def create_order_endpoint(order_data: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db=db, order_data=order_data)

@app.get("/order-details/{order_id}")
def get_order_endpoint(order_id: int, db: Session = Depends(get_db)):
    db_order = get_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@app.put("/orders/{order_id}")
def update_order_endpoint(order_id: int, order_data: OrderUpdate, db: Session = Depends(get_db)):
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
def create_batch_endpoint(batch_data: BatchCreate, db: Session = Depends(get_db)):
    return create_batch(db=db, batch_data=batch_data)

@app.get("/batches/{batch_id}")
def get_batch_endpoint(batch_id: int, db: Session = Depends(get_db)):
    db_batch = get_batch(db, batch_id)
    if db_batch is None:
        raise HTTPException(status_code=404, detail="Batch not found")
    return db_batch

@app.put("/batches/{batch_id}")
def update_batch_endpoint(batch_id: int, batch_data: BatchUpdate, db: Session = Depends(get_db)):
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
def create_compound_endpoint(compound_data: CompoundCreate, db: Session = Depends(get_db)):
    return create_compound(db=db, compound_data=compound_data)

@app.get("/compounds/{compound_id}")
def get_compound_endpoint(compound_id: int, db: Session = Depends(get_db)):
    db_compound = get_compound(db, compound_id)
    if db_compound is None:
        raise HTTPException(status_code=404, detail="Compound not found")
    return db_compound

@app.put("/compounds/{compound_id}")
def update_compound_endpoint(compound_id: int, compound_data: CompoundUpdate, db: Session = Depends(get_db)):
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

# Scientists Endpoints
@app.post("/scientists/")
def create_scientist_endpoint(scientist_data: ScientistCreate, db: Session = Depends(get_db)):
    return create_scientist(db=db, scientist_data=scientist_data)

@app.get("/scientists/")
def get_scientists(db: Session = Depends(get_db)):
    return get_all_scientists(db)

@app.get("/scientists/{scientist_id}")
def get_scientist_endpoint(scientist_id: int, db: Session = Depends(get_db)):
    db_scientist = get_scientist(db, scientist_id)
    if db_scientist is None:
        raise HTTPException(status_code=404, detail="Scientist not found")
    return db_scientist

@app.put("/scientists/{scientist_id}")
def update_scientist_endpoint(scientist_id: int, scientist_data: ScientistUpdate, db: Session = Depends(get_db)):
    db_scientist = update_scientist(db, scientist_id, scientist_data)
    if db_scientist is None:
        raise HTTPException(status_code=404, detail="Scientist not found")
    return db_scientist

@app.delete("/scientists/{scientist_id}")
def delete_scientist_endpoint(scientist_id: int, db: Session = Depends(get_db)):
    db_scientist = delete_scientist(db, scientist_id)
    if db_scientist is None:
        raise HTTPException(status_code=404, detail="Scientist not found")
    return db_scientist

# Dispatchers Endpoints
@app.post("/dispatchers/")
def create_dispatcher_endpoint(dispatcher_data: DispatcherCreate, db: Session = Depends(get_db)):
    return create_dispatcher(db=db, dispatcher_data=dispatcher_data)

@app.get("/dispatchers/{dispatcher_id}")
def get_dispatcher_endpoint(dispatcher_id: int, db: Session = Depends(get_db)):
    db_dispatcher = get_dispatcher(db, dispatcher_id)
    if db_dispatcher is None:
        raise HTTPException(status_code=404, detail="Dispatcher not found")
    return db_dispatcher

@app.put("/dispatchers/{dispatcher_id}")
def update_dispatcher_endpoint(dispatcher_id: int, dispatcher_data: DispatcherUpdate, db: Session = Depends(get_db)):
    db_dispatcher = update_dispatcher(db, dispatcher_id, dispatcher_data)
    if db_dispatcher is None:
        raise HTTPException(status_code=404, detail="Dispatcher not found")
    return db_dispatcher

@app.delete("/dispatchers/{dispatcher_id}")
def delete_dispatcher_endpoint(dispatcher_id: int, db: Session = Depends(get_db)):
    db_dispatcher = delete_dispatcher(db, dispatcher_id)
    if db_dispatcher is None:
        raise HTTPException(status_code=404, detail="Dispatcher not found")
    return db_dispatcher

# Projects Endpoints
@app.post("/projects/")
def create_project_endpoint(project_data: ProjectCreate, db: Session = Depends(get_db)):
    return create_project(db=db, project_data=project_data)

@app.get("/projects/")
def get_projects(db: Session = Depends(get_db)):
    return get_all_projects(db)

@app.get("/projects/{project_id}")
def get_project_endpoint(project_id: int, db: Session = Depends(get_db)):
    db_project = get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@app.put("/projects/{project_id}")
def update_project_endpoint(project_id: int, project_data: ProjectUpdate, db: Session = Depends(get_db)):
    db_project = update_project(db, project_id, project_data)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@app.delete("/projects/{project_id}")
def delete_project_endpoint(project_id: int, db: Session = Depends(get_db)):
    db_project = delete_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

# Targets Endpoints
@app.post("/targets/")
def create_target_endpoint(target_data: TargetCreate, db: Session = Depends(get_db)):
    return create_target(db=db, target_data=target_data)

@app.get("/targets/{target_id}")
def get_target_endpoint(target_id: int, db: Session = Depends(get_db)):
    db_target = get_target(db, target_id)
    if db_target is None:
        raise HTTPException(status_code=404, detail="Target not found")
    return db_target

@app.put("/targets/{target_id}")
def update_target_endpoint(target_id: int, target_data: TargetUpdate, db: Session = Depends(get_db)):
    db_target = update_target(db, target_id, target_data)
    if db_target is None:
        raise HTTPException(status_code=404, detail="Target not found")
    return db_target

@app.delete("/targets/{target_id}")
def delete_target_endpoint(target_id: int, db: Session = Depends(get_db)):
    db_target = delete_target(db, target_id)
    if db_target is None:
        raise HTTPException(status_code=404, detail="Target not found")
    return db_target

# CheckInOut Endpoints
@app.post("/checkinouts/")
def create_checkinout_endpoint(checkinout_data: CheckInOutCreate, db: Session = Depends(get_db)):
    return create_checkinout(db=db, checkinout_data=checkinout_data)

@app.get("/checkinouts/{checkinout_id}")
def get_checkinout_endpoint(checkinout_id: int, db: Session = Depends(get_db)):
    db_checkinout = get_checkinout(db, checkinout_id)
    if db_checkinout is None:
        raise HTTPException(status_code=404, detail="CheckInOut not found")
    return db_checkinout

@app.put("/checkinouts/{checkinout_id}")
def update_checkinout_endpoint(checkinout_id: int, checkinout_data: CheckInOutUpdate, db: Session = Depends(get_db)):
    db_checkinout = update_checkinout(db, checkinout_id, checkinout_data)
    if db_checkinout is None:
        raise HTTPException(status_code=404, detail="CheckInOut not found")
    return db_checkinout

@app.delete("/checkinouts/{checkinout_id}")
def delete_checkinout_endpoint(checkinout_id: int, db: Session = Depends(get_db)):
    db_checkinout = delete_checkinout(db, checkinout_id)
    if db_checkinout is None:
        raise HTTPException(status_code=404, detail="CheckInOut not found")
    return db_checkinout