from fastapi import APIRouter
from app.api.routes import audio, messages, voice

router = APIRouter()

router.include_router(audio.router)
router.include_router(messages.router)
router.include_router(voice.router)