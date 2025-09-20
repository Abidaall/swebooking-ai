from fastapi import APIRouter

router = APIRouter()

@router.post("/peppol/send")
def send_peppol(invoice: dict):
    # Placeholder: validate minimal fields and return mock response
    required = {"invoiceNumber", "issueDate", "seller", "buyer", "lines"}
    missing = [k for k in required if k not in invoice]
    if missing:
        return {"status": "error", "missing": missing}
    return {"status": "queued", "transport": "peppol_sandbox"}
