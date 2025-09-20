# Extremely simplified "AI" classifier placeholder.
# In production, replace with a trained model and a rules engine for Swedish VAT/BAS.
KEYWORDS = {
    "lunch": (6071, "6"),
    "hotel": (5830, "12"),
    "taxi": (5611, "6"),
    "flight": (5800, "6"),
    "spotify": (6230, "25"),
    "ad": (5910, "25"),
    "swish": (1930, None),
    "stripe": (1930, None),
    "ticket": (3051, "6"),  # entré 6 % (exempel, kontrollera reglerna per case)
}

def suggest(description: str, amount: float):
    desc = description.lower()
    for k, (acct, vat) in KEYWORDS.items():
        if k in desc:
            # naive direction: positive = expense -> debit cost; credit bank/kassa later during reconciliation
            debit = acct
            credit = 2440 if amount > 0 else 1510
            return {"debit": debit, "credit": credit, "vat_rate": vat}
    # fallback
    return {"debit": 6570, "credit": 2440, "vat_rate": "25"}  # övriga externa kostnader
