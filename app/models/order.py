from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    OrderID = Column(Integer, primary_key=True, index=True)
    ScientistID = Column(Integer, ForeignKey("scientists.ScientistID"))
    DispatcherID = Column(Integer, ForeignKey("dispatchers.DispatcherId"))
    ShipmentDate = Column(DateTime)
    TrackingID = Column(String, index=True)
    NoOfShipments = Column(Integer)
    Comments = Column(String)
    isComplete = Column(Boolean, default=False)

    # Relationships
    batches = relationship("Batch", back_populates="order")
    dispatcher = relationship("Dispatcher", back_populates="orders")
    scientist = relationship("Scientist", back_populates="orders")