from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    ProjectID = Column(Integer, primary_key=True, index=True)
    ProjectName = Column(String, index=True)

     # Relationship with batch
    batches = relationship("Batch", back_populates="project")

