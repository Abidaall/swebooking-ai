# Placeholder for OCR pipeline; in production use a vendor SDK or Tesseract with pre/post-processing.
def extract_fields_from_receipt(text: str):
    # naive parse
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    description = lines[0] if lines else "Receipt"
    total = 0.0
    for l in lines:
        if "TOTAL" in l.upper() or "SUMMA" in l.upper():
            nums = [s for s in l.split() if s.replace(',','.',1).replace('-','',1).replace('.','',1).isdigit()]
            if nums:
                total = float(nums[-1].replace(',','.'))
    return {"description": description, "amount": total or 0.0, "currency": "SEK"}
