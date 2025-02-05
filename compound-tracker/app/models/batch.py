from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

# Batch Class
class Batch(Base):
    __tablename__ = "batches"

    BatchId = Column(Integer, primary_key=True, index=True)
    OrderId = Column(Integer, ForeignKey("orders.OrderID"))
    #TargetID = Column(Integer, ForeignKey("targets.TargetID"))
    #ScientistID = Column(Integer, ForeignKey("scientists.ScientistID"))
    Project = Column(String)
    IsPhysicallyReceived = Column(Boolean)
    ReceivedDate = Column(DateTime)
    IsCDDRegistered = Column(Boolean)
    CDDRegisteredDate = Column(DateTime)
    CDDImportFileName = Column(String)
    IsInitialCheckedOut = Column(Boolean)
    Comments = Column(String)
    S3PlateMapLocation = Column(String)

    # Relationships
    order = relationship("Order", back_populates="batches")
    #target = relationship("Target", back_populates="batches")
    #scientist = relationship("Scientist", back_populates="batches")
    compounds = relationship("Compound", back_populates="batch")
    #checkins = relationship("CheckInOut", back_populates="batch")