from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


# Compound Class
class Compound(Base):
    __tablename__ = "compounds"

    CompoundId = Column(Integer, primary_key=True, index=True)
    BatchId = Column(Integer, ForeignKey("batches.BatchId"))
    SACCId = Column(String, index=True)
    Concentration = Column(String)
    InitialAmount = Column(Integer)
    CurrentAmountLeft = Column(Integer)
    #ProjectId = Column(Integer, ForeignKey("projects.id"))

    # Relationships
    batch = relationship("Batch", back_populates="compounds")
