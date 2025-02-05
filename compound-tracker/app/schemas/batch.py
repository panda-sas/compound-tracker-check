# app/schemas/batch.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Create schema for creating a batch
class BatchCreate(BaseModel):
    OrderId: int
    Target: str
    Location: str
    Scientist: str
    Project: str
    IsPhysicallyReceived: bool
    ReceivedDate: Optional[datetime]
    IsCDDRegistered: bool
    CDDRegisteredDate: Optional[datetime]
    CDDImportFileName: Optional[str]
    IsInitialCheckedOut: bool
    Comments: Optional[str]
    S3PlateMapLocation: Optional[str]

    class Config:
        orm_mode = True

# Update schema for updating a batch
class BatchUpdate(BaseModel):
    Target: Optional[str]
    Location: Optional[str]
    Scientist: Optional[str]
    Project: Optional[str]
    IsPhysicallyReceived: Optional[bool]
    ReceivedDate: Optional[datetime]
    IsCDDRegistered: Optional[bool]
    CDDRegisteredDate: Optional[datetime]
    CDDImportFileName: Optional[str]
    IsInitialCheckedOut: Optional[bool]
    Comments: Optional[str]
    S3PlateMapLocation: Optional[str]

    class Config:
        orm_mode = True
