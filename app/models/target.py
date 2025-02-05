# Target Class

from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Target(Base):
    __tablename__ = "targets"

    TargetID = Column(Integer, primary_key=True, index=True)
    TargetName = Column(String, index=True)

    # Relationship with Batch
    batches = relationship("Batch", back_populates="target")