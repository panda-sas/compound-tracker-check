from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CheckInOutBase(BaseModel):
    BatchId: int
    ScientistID: int
    CheckoutDate: datetime
    TentativeReturnDate: datetime
    Purpose: str
    IsReturned: bool = False
    ActualReturnDate: Optional[datetime] = None
    IsResultedUploadedToCDD: bool = False
    CDDResultURL: Optional[str] = None
    Reviewer: Optional[str] = None
    IsReviewed: bool = False
    ReviewDate: Optional[datetime] = None
    Comments: Optional[str] = None
    IsPlateCreated: bool = False

class CheckInOutCreate(CheckInOutBase):
    pass

class CheckInOutUpdate(CheckInOutBase):
    CheckoutDate: Optional[datetime] = None
    TentativeReturnDate: Optional[datetime] = None
    Purpose: Optional[str] = None
    IsReturned: Optional[bool] = None
    ActualReturnDate: Optional[datetime] = None
    IsResultedUploadedToCDD: Optional[bool] = None
    CDDResultURL: Optional[str] = None
    Reviewer: Optional[str] = None
    IsReviewed: Optional[bool] = None
    ReviewDate: Optional[datetime] = None
    Comments: Optional[str] = None
    IsPlateCreated: Optional[bool] = None

class CheckInOut(CheckInOutBase):
    CheckOutId: int

    class Config:
        orm_mode = True
