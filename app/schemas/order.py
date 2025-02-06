from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OrderBase(BaseModel):
    ScientistID: int
    DispatcherID: int
    ShipmentDate: datetime
    TrackingID: str
    NoOfShipments: int
    Comments: Optional[str] = None
    isComplete: bool

    class Config:
        orm_mode = True

class OrderCreate(BaseModel):
    ScientistID: int  # Ensure this is an integer
    DispatcherID: int  # Ensure this is an integer
    ShipmentDate: datetime
    TrackingID: str
    NoOfShipments: int
    Comments: Optional[str] = None
    isComplete: bool

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

class Order(OrderBase):
    OrderID: int

    class Config:
        orm_mode = True
