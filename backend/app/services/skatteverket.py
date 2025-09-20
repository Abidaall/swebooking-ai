# Mock client for Skatteverket. Replace with real API calls (AGI open API when applicable, file transfer for SRU, etc.).
import os

def submit_agi(payload: dict):
    api_key = os.getenv("SKATTEVERKET_API_KEY", "dev-key")
    # pretend to send
    return {"status": "submitted", "via": "mock_api", "api_key_set": bool(api_key), "payload_preview": list(payload.keys())}

def submit_vat(payload: dict):
    # Until moms-API is live, this would be file transfer or manual export.
    return {"status": "generated", "channel": "file_transfer_placeholder", "period": payload.get("period")}
