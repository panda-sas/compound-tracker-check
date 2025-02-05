
# CheckInOut Class
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

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