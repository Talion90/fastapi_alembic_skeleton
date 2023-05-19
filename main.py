import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings


app = FastAPI()


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    config = uvicorn.Config(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True,
    )
    server = uvicorn.Server(config)
    server.run()
