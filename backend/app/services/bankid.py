# Mock BankID flows; in production integrate against BankID Relying Party API.
import uuid

def auth_start(personnummer: str):
    return {"orderRef": str(uuid.uuid4()), "status": "pending", "hint": "Open BankID app to sign (mock)"}

def auth_collect(order_ref: str):
    # For demo: instantly complete
    return {"orderRef": order_ref, "status": "complete", "user": {"pnr": "19010101-1234"}}
