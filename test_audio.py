import aiofiles
import asyncio
import httpx

API_URL = "http://localhost:8000/api/procesar-audio"
AUDIO_PATH = "test_audio.wav"

async def probar_transcripcion():
    async with aiofiles.open(AUDIO_PATH, "rb") as f:
        audio_bytes = await f.read()

    files = {
        "file": (AUDIO_PATH, audio_bytes, "audio/wav")
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, files=files)
        response.raise_for_status()

if __name__ == "__main__":
    asyncio.run(probar_transcripcion())
