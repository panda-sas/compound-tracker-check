from pydantic import BaseModel
from typing import Optional

class DispatcherBase(BaseModel):
    DispatcherName: str

class DispatcherCreate(DispatcherBase):
    pass

class DispatcherUpdate(DispatcherBase):
    DispatcherName: Optional[str] = None

class Dispatcher(DispatcherBase):
    DispatcherId: int

    class Config:
        orm_mode = True
