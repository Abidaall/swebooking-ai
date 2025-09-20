from fastapi import APIRouter
from ..services import skatteverket

router = APIRouter()

@router.post("/submit")
def submit_agi(dummy_payload: dict):
    # Replace with real AGI schema
    return skatteverket.submit_agi(dummy_payload)
