from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderCreate(BaseModel):
    Scientist: str
    Dispatcher: str
    ShipmentDate: datetime
    TrackingID: str
    NoOfShipments: int
    Comments: Optional[str] = None
    isComplete: bool = False

    class Config:
        orm_mode = True  # Tells Pydantic to work with SQLAlchemy models

class OrderUpdate(BaseModel):
    Scientist: Optional[str] = None
    Dispatcher: Optional[str] = None
    ShipmentDate: Optional[datetime] = None
    TrackingID: Optional[str] = None
    NoOfShipments: Optional[int] = None
    Comments: Optional[str] = None
    isComplete: Optional[bool] = None

    class Config:
        orm_mode = True

class OrderResponse(OrderCreate):
    OrderID: int

    class Config:
        orm_mode = True
