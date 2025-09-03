from elevenlabs.client import ElevenLabs
import logging
from app.config.settings import settings

logger = logging.getLogger(__name__)

class ElevenLabsClient:
    def __init__(self):
        self.client = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)
    
    async def generar_audio(self, texto: str) -> bytes:
        """Convertir texto a audio usando ElevenLabs v2"""
        try:
            # Nueva sintaxis v2
            response = self.client.text_to_speech.convert(
                voice_id=settings.ELEVENLABS_VOICE_ID,
                optimize_streaming_latency="0",
                output_format="mp3_44100_128",
                text=texto,
                model_id="eleven_multilingual_v2"
            )
            
            # Convertir a bytes
            audio_bytes = b"".join(response)
            logger.info(f"Audio generado para texto: {texto[:50]}...")
            
            return audio_bytes
            
        except Exception as e:
            logger.error(f"Error generando audio: {str(e)}")
            raise RuntimeError(f"Error generando audio: {str(e)}")

elevenlabs_client = ElevenLabsClient()