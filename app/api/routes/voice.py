from app.core.models import TextToSpeechRequest
from app.utils.elevenlabs_client import elevenlabs_client
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response

router = APIRouter(prefix="/voice", tags=["voice"])

@router.post("/text-to-speech", response_class=Response)
def text_to_speech(request: TextToSpeechRequest):
    try:
        audio = elevenlabs_client.generate_audio(request.text)
        return Response(content=audio, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
