from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    OrderID = Column(Integer, primary_key=True, index=True)
    Scientist = Column(String, index=True)
    Dispatcher = Column(String)
    ShipmentDate = Column(DateTime)
    TrackingID = Column(String, index=True)
    NoOfShipments = Column(Integer)
    Comments = Column(String)
    isComplete = Column(Boolean, default=False)

    batches = relationship("Batch", back_populates="order")
