from fastapi import APIRouter, UploadFile, File
from app.services.audio_service import AudioService
from app.core.models import AudioResponse

router = APIRouter(prefix="/audio", tags=["audio"])

@router.post("/process", response_model=AudioResponse)
async def process_audio(file: UploadFile = File(...)):
    try:
        return await AudioService.process_audio(file)
    except Exception as e:
        # Agrega logging aquí también
        print("❌ Error en router audio:", str(e))
        raise