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


# Target Class
class Target(Base):
    __tablename__ = "targets"

    TargetID = Column(Integer, primary_key=True, index=True)
    TargetName = Column(String, index=True)

    # Relationship with Batch
    batches = relationship("Batch", back_populates="target")


# Scientist Class
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


# Order Class
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


# Batch Class
class Batch(Base):
    __tablename__ = "batches"

    BatchId = Column(Integer, primary_key=True, index=True)
    OrderId = Column(Integer, ForeignKey("orders.OrderID"))
    TargetID = Column(Integer, ForeignKey("targets.TargetID"))
    ScientistID = Column(Integer, ForeignKey("scientists.ScientistID"))
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
    target = relationship("Target", back_populates="batches")
    scientist = relationship("Scientist", back_populates="batches")
    compounds = relationship("Compound", back_populates="batch")
    checkins = relationship("CheckInOut", back_populates="batch")


# Compound Class
class Compound(Base):
    __tablename__ = "compounds"

    CompoundId = Column(Integer, primary_key=True, index=True)
    BatchId = Column(Integer, ForeignKey("batches.BatchId"))
    SACCId = Column(String, index=True)
    Concentration = Column(String)
    InitialAmount = Column(Integer)
    CurrentAmountLeft = Column(Integer)
    ProjectId = Column(Integer, ForeignKey("projects.id"))

    # Relationships
    batch = relationship("Batch", back_populates="compounds")
    project = relationship("Project", back_populates="compounds")


# CheckInOut Class
class CheckInOut(Base):
    __tablename__ = "checkinout"

    CheckOutId = Column(Integer, primary_key=True, index=True)
    BatchId = Column(Integer, ForeignKey("batches.BatchId"))
    ScientistID = Column(Integer, ForeignKey("scientists.ScientistID"))
    CheckoutDate = Column(DateTime)
    TentativeReturnDate = Column(DateTime)
    Purpose = Column(String)
    IsReturned = Column(Boolean, default=False)
    ActualReturnDate = Column(DateTime)
    IsResultedUploadedToCDD = Column(Boolean, default=False)
    CDDResultURL = Column(String)
    Reviewer = Column(String)
    IsReviewed = Column(Boolean, default=False)
    ReviewDate = Column(DateTime)
    Comments = Column(String)
    IsPlateCreated = Column(Boolean, default=False)

    # Relationships
    batch = relationship("Batch", back_populates="checkins")
    scientist = relationship("Scientist", back_populates="checkins")
