from pydantic.v1 import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    URL: str

    class Config:
        env_file = ".env"


settings = Settings()
