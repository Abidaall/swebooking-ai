from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..models.transaction import Transaction
from ..models.account import Account
from ..schemas.common import TransactionIn, TransactionOut
from ..services.ai_classifier import suggest
from datetime import date

router = APIRouter()

@router.post("/", response_model=TransactionOut)
def create(tx: TransactionIn, db: Session = Depends(get_db)):
    # Suggest accounts and VAT based on description/amount
    s = suggest(tx.description, tx.amount)
    # Ensure accounts exist (naively create if missing for demo)
    for acct_id in [s["debit"], s["credit"]]:
        if acct_id and not db.get(Account, acct_id):
            db.add(Account(id=acct_id, name=f"Konto {acct_id}"))
    t = Transaction(
        date=tx.date,
        description=tx.description,
        amount=tx.amount,
        currency=tx.currency,
        debit_account_id=s["debit"],
        credit_account_id=s["credit"],
        vat_rate=s["vat_rate"],
        supplier=tx.supplier,
        customer=tx.customer,
    )
    db.add(t)
    db.commit()
    db.refresh(t)
    return t

@router.get("/", response_model=list[TransactionOut])
def list_transactions(from_date: date | None = None, to_date: date | None = None, db: Session = Depends(get_db)):
    q = db.query(Transaction)
    if from_date: q = q.filter(Transaction.date >= from_date)
    if to_date: q = q.filter(Transaction.date <= to_date)
    return q.order_by(Transaction.date.desc()).all()
