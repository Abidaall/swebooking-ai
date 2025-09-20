from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..models.transaction import Transaction
from ..services.vat import accumulate
from ..services import skatteverket

router = APIRouter()

@router.get("/preview")
def preview(period: str, db: Session = Depends(get_db)):
    # naive period filter: YYYY-MM for month
    year, month = period.split("-")
    txs = db.query(Transaction).filter(Transaction.date.like(f"{year}-{month}-%")).all()
    payload = [{
        "amount": float(t.amount),
        "vat_rate": t.vat_rate
    } for t in txs]
    totals = accumulate(payload)
    return {"period": period, "totals": totals, "transactions": len(txs)}

@router.post("/submit")
def submit(period: str, db: Session = Depends(get_db)):
    # In real life: build proper VAT declaration payload incl. boxes
    preview_data = preview(period, db)
    result = skatteverket.submit_vat({"period": period, "preview": preview_data})
    return result
