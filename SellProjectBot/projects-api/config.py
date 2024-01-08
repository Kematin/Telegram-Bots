from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    JWT_SECRET_KEY: str
    DATABASE_URL: str
    CATEGORIES: dict = Field({"full11": 1, "full9": 2, "minimum": 3})

    class Config:
        env_file = ".env"


config = Settings()
