from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
  DEEPGRAM_API_KEY: str = os.getenv("DEEPGRAM_API_KEY")
  DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")
  ELEVENLABS_API_KEY: str = os.getenv("ELEVENLABS_API_KEY")
  OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
  SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")
  SUPABASE_URL: str = os.getenv("SUPABASE_URL")
  
  APP_ENV: str = os.getenv("APP_ENV", "development")
  
  class Config:
    env_file = ".env"

settings = Settings()