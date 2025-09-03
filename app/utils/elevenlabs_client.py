from app.config.settings import settings
from elevenlabs.client import ElevenLabs

class ElevenLabsClient:
    def __init__(self):
        self.client = ElevenLabs(api_key=settings.ELEVENLABS_API_KEY)
    
    def generate_audio(self, text: str) -> bytes:
        """Convertir texto a audio usando ElevenLabs v2"""
        try:
            response = self.client.text_to_speech.convert(
                voice_id=settings.ELEVENLABS_VOICE_ID,
                optimize_streaming_latency="0",
                output_format="mp3_44100_128",
                text=text,
                model_id="eleven_multilingual_v2"
            )

            audio_bytes = b"".join(response)
            
            return audio_bytes
            
        except Exception as e:
            raise RuntimeError(f"Error generando audio: {str(e)}")

elevenlabs_client = ElevenLabsClient()