from fastapi import APIRouter
from . import transactions, vat, agi, invoices, auth

router = APIRouter()
router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
router.include_router(vat.router, prefix="/vat", tags=["vat"])
router.include_router(agi.router, prefix="/agi", tags=["agi"])
router.include_router(invoices.router, prefix="/invoices", tags=["invoices"])
