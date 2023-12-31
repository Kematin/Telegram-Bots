from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str
    JWT_SECRET_KEY: str
    DATABASE_URL: str
    CATEGORIES: dict = Field({"full11": 1, "full9": 2, "minimum": 3})
    FILE_TYPES: dict = Field(
        {
            "doc": "document.doc",
            "pptx": "presentation.pptx",
            "png": "unique.png",
            "product": "product",
        }
    )
    PROJECT_FIELDS: dict = Field(
        {"pptx": "have_presentation", "png": "have_unique", "product": "have_product"}
    )

    class Config:
        env_file = ".env"


config = Settings()
