import os
from pydantic import BaseModel

class Settings(BaseModel):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./app.db")
    SKATTEVERKET_API_KEY: str = os.getenv("SKATTEVERKET_API_KEY", "dev-key")
    BANKID_ENV: str = os.getenv("BANKID_ENV", "sandbox")
    APP_SECRET_KEY: str = os.getenv("APP_SECRET_KEY", "dev-secret")

settings = Settings()
