from pydantic import BaseModel
from typing import Optional

class ProjectBase(BaseModel):
    ProjectName: str

    class Config:
        orm_mode = True

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    ProjectName: Optional[str] = None

class Project(ProjectBase):
    ProjectId: int

    class Config:
        orm_mode = True
