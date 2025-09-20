from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from ..db.base import Base

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    amount = Column(Numeric(12,2), nullable=False)  # positive expense, negative income or vice-versa based on policy
    currency = Column(String, default="SEK")
    debit_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)
    credit_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)
    vat_rate = Column(String, nullable=True)  # '25','12','6','0','reverse'
    supplier = Column(String, nullable=True)
    customer = Column(String, nullable=True)

    debit_account = relationship("Account", foreign_keys=[debit_account_id])
    credit_account = relationship("Account", foreign_keys=[credit_account_id])
