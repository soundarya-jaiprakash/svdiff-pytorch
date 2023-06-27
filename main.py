from fastapi import FastAPI
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from fastapi.responses import FileResponse
import uvicorn

# Initialize the FastAPI app
app = FastAPI()

# Preload Bark models
preload_models()

@app.post("/prompt-req")
def prompt_req(prompt: str):
    
    audio_array = generate_audio(prompt)

    write_wav("audio_file.wav", SAMPLE_RATE, audio_array)
    
    return FileResponse("audio_file.wav", media_type="audio/wav")

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
