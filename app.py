from fastapi import FastAPI

from routes.health import router as health_router
from routes.ai import router as ai_router

app = FastAPI()

app.include_router(health_router)
app.include_router(ai_router)