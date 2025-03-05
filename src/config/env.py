from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic_settings import BaseSettings

PROJECT_ROOT = Path(__file__).parents[2]


class App(BaseModel):
    LOG_LEVEL: Literal["debug", "info", "warning", "error", "critical"] = "debug"
    GROQ_API_KEY: str
    DATABASE_URL: str    
    X_ACCESS_KEY: str
    X_ACCESS_SECRET: str
    X_CONSUMER_KEY: str
    X_CONSUMER_SECRET: str
    

class Settings(BaseSettings):
    APP: App

    class Config:
        case_sensitive: bool = True
        env_nested_delimiter: str = "__"
        env_file_encoding: str = "utf-8"
        env_file = PROJECT_ROOT / ".env"
        use_enum_values = True


settings = Settings()