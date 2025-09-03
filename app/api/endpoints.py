from pydantic import BaseModel
from app.config.settings import settings
from app.core.models import AudioResponse, HealthResponse
from app.utils.deepgram_client import deepgram_client
from app.utils.elevenlabs_client import elevenlabs_client
from fastapi import APIRouter, File, HTTPException, Response, UploadFile
from fastapi.responses import FileResponse
import logging
import os

logger = logging.getLogger(__name__)
router = APIRouter()

api_key = os.getenv("ELEVENLABS_API_KEY")
if not api_key:
    raise RuntimeError("ELEVENLABS_API_KEY no está definida en el entorno")

class TextToSpeechRequest(BaseModel):
    text: str

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

@router.post("/procesar-audio", response_model=AudioResponse)
async def procesar_audio(file: UploadFile = File(...)):
  """Procesar audio y transcribir a texto usando DeepGram"""
  try:
    if not deepgram_client.dg_client:
      raise HTTPException(status_code=500, detail="DeepGram no configurado")
    
    # Leer audio como BYTES
    audio_buffer = await file.read()
    
    # Asegurar que son bytes, no string
    if isinstance(audio_buffer, str):
      audio_buffer = audio_buffer.encode('utf-8')
    
    # Transcribir audio
    texto = await deepgram_client.transcribir_audio(
      audio_buffer, 
      mimetype=file.content_type
    )
    
    return AudioResponse(
      texto=texto,
      status="success"
    )
      
  except Exception as e:
    logger.error(f"Error procesando audio: {str(e)}")
    raise HTTPException(status_code=500, detail=str(e))

# app/api/endpoints.py
from app.utils.elevenlabs_client import elevenlabs_client

class TextToSpeechRequest(BaseModel):
    text: str

@router.post("/texto-a-audio", response_class=Response)
async def texto_a_audio(request: TextToSpeechRequest):
    """Convertir texto a audio"""
    try:
        audio = await elevenlabs_client.generar_audio(request.text)
        return Response(content=audio, media_type="audio/mpeg")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
