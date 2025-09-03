from app.config.settings import settings
from app.core.models import AudioResponse, HealthResponse, OrderRequest, TextToSpeechRequest, UserMessageRequest
from app.utils.supabase_client import supabase_client
from app.utils.deepgram_client import deepgram_client
from app.utils.elevenlabs_client import elevenlabs_client
from fastapi import APIRouter, File, HTTPException, Response, UploadFile
import logging
import os

logger = logging.getLogger(__name__)
router = APIRouter()

api_key = os.getenv("ELEVENLABS_API_KEY")
if not api_key:
    raise RuntimeError("ELEVENLABS_API_KEY no está definida en el entorno")


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


@router.post("/process-audio", response_model=AudioResponse)
async def process_audio(file: UploadFile = File(...)):
  """Procesar audio y transcribir a texto usando DeepGram"""
  try:
    if not deepgram_client.dg_client:
      raise HTTPException(status_code=500, detail="DeepGram no configurado")

    audio_buffer = await file.read()

    if isinstance(audio_buffer, str):
      audio_buffer = audio_buffer.encode('utf-8')

    texto = await deepgram_client.transcribe_audio(
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


@router.post("/text-to-speech", response_class=Response)
async def text_to_speech(request: TextToSpeechRequest):
    """Convertir texto a audio"""
    try:
        audio = elevenlabs_client.generate_audio(request.text)
        return Response(content=audio, media_type="audio/mpeg")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/save-order")
def save_order(order: OrderRequest):
    """Save order to Supabase database"""
    try:
        result = supabase_client.save_order(order.dict())
        return {"status": "success", "order_id": result.get('id')}
        
    except Exception as e:
        logger.error(f"Error saving order: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/save-user-message")
def save_user_message(request: UserMessageRequest):
    """Save user message to database"""
    try:
        # Guardar en Supabase
        response = supabase_client.client.table('user_messages').insert({
            "user_message": request.message
        }).execute()
        
        return {"status": "success", "message_id": response.data[0]['id'] if response.data else None}
        
    except Exception as e:
        logger.error(f"Error saving user message: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/welcome-message")
def get_welcome_message():
    """Get AI welcome message"""
    welcome_text = """
    ¡Bienvenido a nuestro restaurante!
    Es un placer tenerle aquí. 
    ¿Le gustaría que le recomiende algún plato especial del día 
    o prefiere conocer nuestra carta completa?
    """
    
    return {"message": welcome_text}
