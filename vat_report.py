from sqlalchemy import Column, Integer, String, Date, Numeric
from ..db.base import Base

class VATReport(Base):
    __tablename__ = "vat_reports"
    id = Column(Integer, primary_key=True, index=True)
    period = Column(String, nullable=False)  # e.g. '2025-08' (månad) eller '2025Q3'
    sales_25 = Column(Numeric(12,2), default=0)
    sales_12 = Column(Numeric(12,2), default=0)
    sales_6 = Column(Numeric(12,2), default=0)
    vat_out = Column(Numeric(12,2), default=0)
    vat_in = Column(Numeric(12,2), default=0)
    created_at = Column(Date, nullable=True)
