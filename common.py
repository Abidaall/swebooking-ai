from pydantic import BaseModel
from datetime import date
from typing import Optional

class TransactionIn(BaseModel):
    date: date
    description: str
    amount: float
    currency: str = "SEK"
    supplier: Optional[str] = None
    customer: Optional[str] = None

class TransactionOut(BaseModel):
    id: int
    date: date
    description: str
    amount: float
    currency: str
    debit_account_id: int | None
    credit_account_id: int | None
    vat_rate: str | None
    supplier: str | None
    customer: str | None

    class Config:
        from_attributes = True
