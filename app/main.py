from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import router as api_router
from app.config.settings import settings

app = FastAPI(
  title="Alybe AI Backend",
  description="Backend para el mesero virtual IA",
  version="1.0.0"
)

# CORS
app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:3000", "https://tu-frontend.vercel.app"],
  allow_methods=["*"],
  allow_headers=["*"],
)

# Incluir routers
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
  return {"message": "Alybe AI Backend funcionando", "environment": settings.APP_ENV}

@app.get("/health")
async def health_check():
  return {"status": "ok", "service": "alybe-ai-backend"}