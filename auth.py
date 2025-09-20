from fastapi import APIRouter
from ..services import bankid

router = APIRouter()

@router.post("/bankid/start")
def start(pnr: str):
    return bankid.auth_start(pnr)

@router.get("/bankid/collect/{order_ref}")
def collect(order_ref: str):
    return bankid.auth_collect(order_ref)
