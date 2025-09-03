from pydantic import BaseModel
from typing import List, Optional

class AudioInput(BaseModel):
  audio_base64: str  # Audio en base64

class PedidoItem(BaseModel):
  nombre: str
  cantidad: int
  precio: float

class PedidoCreate(BaseModel):
  mesa_id: str
  items: List[PedidoItem]
  total: float

class HealthResponse(BaseModel):
  status: str
  deepgram_configured: bool
  elevenlabs_configured: bool
  supabase_configured: bool

class AudioResponse(BaseModel):
  texto: str
  status: str
