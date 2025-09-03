from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
  DEEPGRAM_API_KEY: str
  DEEPSEEK_API_KEY: str
  ELEVENLABS_API_KEY: str
  ELEVENLABS_VOICE_ID: str
  OPENAI_API_KEY: str
  SUPABASE_KEY: str
  SUPABASE_URL: str
  
  class Config:
    env_file = ".env"

settings = Settings()
