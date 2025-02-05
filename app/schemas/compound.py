# app/schemas/compound.py

from pydantic import BaseModel
from typing import Optional

# Create schema for creating a compound
class CompoundCreate(BaseModel):
    BatchId: int
    SACCId: str
    Concentration: Optional[str]
    InitialAmount: int
    CurrentAmountLeft: int

    class Config:
        orm_mode = True

# Update schema for updating a compound
class CompoundUpdate(BaseModel):
    SACCId: Optional[str]
    Concentration: Optional[str]
    InitialAmount: Optional[int]
    CurrentAmountLeft: Optional[int]

    class Config:
        orm_mode = True
