import aiofiles
import asyncio
import requests

async def test_speech_synthesis():
    url = "http://localhost:8000/api/text-to-speech"

    payload = {"text": "Hola, esto es una prueba de síntesis de voz"}
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        async with aiofiles.open("audio_output.mp3", "wb") as f:
            await f.write(response.content)
        print("✅ Audio generado y guardado exitosamente")    
    else:
        print(f"❌ Error: {response.text}")

asyncio.run(test_speech_synthesis())