from pydantic import BaseModel
from typing import Optional

class TargetBase(BaseModel):
    TargetName: str

class TargetCreate(TargetBase):
    pass

class TargetUpdate(TargetBase):
    TargetName: Optional[str] = None

class Target(TargetBase):
    TargetID: int

    class Config:
        orm_mode = True
