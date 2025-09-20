# Extremely simplified reconciliation: match bank strings to open ledger items.
def reconcile(bank_text: str):
    rules = {
        "SWISH": "1930",
        "STRIPE": "1510",
        "IZETTLE": "1510",
        "RENT": "5010",
    }
    for k, acct in rules.items():
        if k in bank_text.upper():
            return {"match": True, "account": int(acct)}
    return {"match": False}
