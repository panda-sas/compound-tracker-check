from pydantic import BaseModel
from typing import Optional

class ScientistBase(BaseModel):
    ScientistName: str
    UIN: str
    Email: str

class ScientistCreate(ScientistBase):
    pass

class ScientistUpdate(ScientistBase):
    ScientistName: Optional[str] = None
    UIN: Optional[str] = None
    Email: Optional[str] = None

class Scientist(ScientistBase):
    ScientistID: int

    class Config:
        orm_mode = True
