from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Centralized configuration object.

    Using environment-based configuration mirrors production security practices
    and prevents accidental hardcoding of secrets.
    """
    DATABASE_URL: str = "postgresql+asyncpg://localhost/gophish"

    class Config:
        env_file = ".env"

settings = Settings()
