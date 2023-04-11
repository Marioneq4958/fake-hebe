import uvicorn
from fastapi import FastAPI

from src.core.config import settings

application: FastAPI = FastAPI()

if __name__ == "__main__":
    uvicorn.run(
        "main:application", host=settings.API_HOST, port=settings.API_PORT, reload=True
    )
