# Scientist Class
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Scientist(Base):
    __tablename__ = "scientists"

    ScientistID = Column(Integer, primary_key=True, index=True)
    ScientistName = Column(String, index=True)
    UIN = Column(String, unique=True)
    Email = Column(String, unique=True)

    # Relationship with Orders and Batches
    orders = relationship("Order", back_populates="scientist")
    batches = relationship("Batch", back_populates="scientist")
    checkins = relationship("CheckInOut", back_populates="scientist")