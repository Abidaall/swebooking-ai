# SweBookkeeping AI (MVP scaffold)

En startklar kodbas för en AI-driven svensk bokföringsapp:
- FastAPI backend
- PostgreSQL via Docker
- BAS-kontoplan (utdrag) + verifikat, momsrapport, leverantörer, kunder
- Mockade integrationer: Skatteverket (AGI/VAT-skiss), BankID, Peppol
- En enkel regelbaserad "AI"-klassificerare som kan föreslå konto + momssats

## Snabbstart
```bash
cp .env.example .env
docker compose up --build
# Öppna http://localhost:8000/docs
```
## Struktur
- `backend/app/models` – SQLAlchemy-modeller
- `backend/app/api` – REST-endpoints (transactions, vat, agi, invoices, auth)
- `backend/app/services` – OCR/AI/regelmotor/mock-klienter
- `backend/app/core` – konfiguration, init
- `backend/app/tests` – enkla tester

> OBS: Detta är en **MVP-skiss** för utveckling/testing. För produktion tillkommer bl.a. riktig BankID-integration,
> Skatteverkets produktionskanaler, Peppol access point, DPIA, loggning och regelefterlevnad.
