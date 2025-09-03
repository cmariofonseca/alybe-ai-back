from pydantic import BaseModel
from typing import List, Optional

class HealthResponse(BaseModel):
  status: str
  deepgram_configured: bool
  elevenlabs_configured: bool
  supabase_configured: bool

class AudioResponse(BaseModel):
  texto: str
  status: str

class TextToSpeechRequest(BaseModel):
  text: str
