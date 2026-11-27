from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url: str = "postgresql://parkos:parkos@postgres:5432/parkos"
    redis_url: str = "redis://redis:6379/0"
    hmac_secret: str = "replace-this-development-secret"
    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:8080"]
    grace_minutes: int = 10
    hold_seconds: int = 60
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
