from decimal import Decimal
from typing import Iterable, Dict

def accumulate(transactions: Iterable[Dict]):
    sales_25 = sales_12 = sales_6 = Decimal("0")
    vat_out = vat_in = Decimal("0")
    for t in transactions:
        amt = Decimal(str(t["amount"]))
        rate = t.get("vat_rate")
        if rate in {"25","12","6"}:
            # naive split: positive amounts -> cost (vat_in), negative -> sale (vat_out) depending on app policy
            if amt < 0:
                base = (amt / (Decimal("1")+Decimal(rate)/100)).copy_abs()
                sales_key = f"sales_{rate}"
                if rate == "25": sales_25 += base
                if rate == "12": sales_12 += base
                if rate == "6": sales_6 += base
                vat_out += (base * Decimal(rate) / 100)
            else:
                base = amt / (Decimal("1")+Decimal(rate)/100)
                vat_in += (base * Decimal(rate) / 100)
        # else: 0%/reverse handled elsewhere
    return {
        "sales_25": float(sales_25),
        "sales_12": float(sales_12),
        "sales_6": float(sales_6),
        "vat_out": float(vat_out),
        "vat_in": float(vat_in),
    }
