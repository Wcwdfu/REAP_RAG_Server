from fastapi import FastAPI
from app.api.endpoints import router as api_router

app = FastAPI()

# API 라우터 등록
app.include_router(api_router)