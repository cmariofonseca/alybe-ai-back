# test_tts.py
import requests
import asyncio
import aiofiles

async def probar_sintesis():
    url = "http://localhost:8000/api/texto-a-audio"
    
    # JSON debe coincidir exactamente con el modelo Pydantic
    payload = {"text": "Hola, esto es una prueba de síntesis de voz"}
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        async with aiofiles.open("audio_output.mp3", "wb") as f:
            await f.write(response.content)
    else:
        print(f"❌ Error: {response.text}")

asyncio.run(probar_sintesis())