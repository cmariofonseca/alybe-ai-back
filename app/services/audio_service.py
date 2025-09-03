from app.core.models import AudioResponse
from app.utils.deepgram_client import deepgram_client
from app.utils.supabase_client import supabase_client
from fastapi import HTTPException, UploadFile
import logging

logger = logging.getLogger(__name__)

class AudioService:
    @staticmethod
    async def process_audio(file: UploadFile) -> AudioResponse:
        print("llegó a process_audio")
        try:
            # ✅ CORREGIR: Usar dg_client en lugar de client
            if not deepgram_client.dg_client:
                raise HTTPException(status_code=500, detail="DeepGram not configured")
            
            print("pasamos el primer if")
            audio_buffer = await file.read()
            text = await deepgram_client.transcribe_audio(
                audio_buffer, 
                mimetype=file.content_type
            )
            
            print("✅ Audio transcribido: ", text)
            
            try:
                response = supabase_client.client.table('user_messages').insert({
                    "user_message": text
                }).execute()
                
                if response.data:
                    print("✅ Mensaje guardado en Supabase con ID:", response.data[0]['id'])
                else:
                    print("⚠️  No se pudo guardar en Supabase")
                    
            except Exception as db_error:
                logger.error(f"Error guardando en Supabase: {db_error}")
            
            return AudioResponse(
                text=text,
                status="success"
            )
            
        except Exception as e:
            print("❌ Error en process_audio:", str(e))
            raise HTTPException(status_code=500, detail=str(e))
