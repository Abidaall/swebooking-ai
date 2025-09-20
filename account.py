from sqlalchemy import Column, Integer, String, Boolean
from ..db.base import Base

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True, index=True)  # BAS kontonummer
    name = Column(String, nullable=False)
    vat_deductible = Column(Boolean, default=True)
    vat_code = Column(String, nullable=True)  # e.g. '25', '12', '6', '0', 'MOSS', etc.
