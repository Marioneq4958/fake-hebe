from pydantic import BaseSettings


class Settings(BaseSettings):
    API_HOST: str = "127.0.0.1"
    API_PORT: int = 8000


settings = Settings()
