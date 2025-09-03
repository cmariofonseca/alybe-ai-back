from pydantic import BaseModel
from typing import List, Optional

class HealthResponse(BaseModel):
  status: str
  deepgram_configured: bool
  elevenlabs_configured: bool
  supabase_configured: bool

class AudioResponse(BaseModel):
  text: str
  status: str

class TextToSpeechRequest(BaseModel):
  text: str


class OrderItem(BaseModel):
    name: str
    quantity: int
    price: float

class OrderCreate(BaseModel):
    table_id: str
    items: List[OrderItem]
    total: float

class OrderRequest(BaseModel):
    table_id: str
    items: List[OrderItem]
    total: float
    status: str = "pending"


class UserMessageRequest(BaseModel):
    message: str
