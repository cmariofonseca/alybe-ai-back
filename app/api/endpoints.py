from app.config.settings import settings
from app.core.models import HealthResponse
from fastapi import APIRouter, HTTPException
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/health", response_model=HealthResponse)
async def health_check():
  """Verificar estado del servicio y configuraciones"""
  try:
    return HealthResponse(
      status="ok",
      deepgram_configured=bool(settings.DEEPGRAM_API_KEY),
      elevenlabs_configured=bool(settings.ELEVENLABS_API_KEY),
      supabase_configured=bool(settings.SUPABASE_URL and settings.SUPABASE_KEY)
    )
  except Exception as e:
    logger.error(f"Health check error: {str(e)}")
    raise HTTPException(status_code=500, detail="Error en health check")