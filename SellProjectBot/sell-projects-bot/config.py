from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    SECRET_KEY: str

    class Config:
        env_file = ".env"


config = Settings()
