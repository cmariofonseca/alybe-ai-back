from app.config.settings import settings
from deepgram import Deepgram

class DeepGramClient:
    def __init__(self):
        if not settings.DEEPGRAM_API_KEY:
            self.dg_client = None
        else:
            self.dg_client = Deepgram(settings.DEEPGRAM_API_KEY)

    async def transcribe_audio(self, audio_buffer: bytes, mimetype: str = "audio/wav") -> str:
        if not self.dg_client:
            raise RuntimeError("Deepgram no configurado correctamente")
        
        try:
            source = {
                'buffer': audio_buffer,
                'mimetype': mimetype
            }

            options = {
                'punctuate': True,
                'language': 'es',
                'model': 'nova',
                'smart_format': True
            }

            response = await self.dg_client.transcription.prerecorded(source, options)
            transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
            return transcript
        
        except Exception as e:
            raise RuntimeError(f"Error transcribiendo audio: {str(e)}")

deepgram_client = DeepGramClient()
