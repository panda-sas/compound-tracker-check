from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Dispatcher Class
class Dispatcher(Base):
    __tablename__ = "dispatchers"

    DispatcherId = Column(Integer, primary_key=True, index=True)
    DispatcherName = Column(String, index=True)

    # Relationship with Order
    orders = relationship("Order", back_populates="dispatcher")