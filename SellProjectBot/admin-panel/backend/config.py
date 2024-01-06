from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    JWT_SECRET_KEY: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"


config = Settings()
