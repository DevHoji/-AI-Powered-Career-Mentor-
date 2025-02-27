from fastapi import APIRouter, UploadFile, File
import whisper
import tempfile
import os

router = APIRouter()
model = whisper.load_model("base")

@router.post("/transcribe")
async def transcribe_audio(audio: UploadFile = File(...)):
    try:
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            content = await audio.read()
            temp_audio.write(content)
            temp_audio.flush()
            
            # Transcribe audio
            result = model.transcribe(temp_audio.name)
            
            # Clean up temporary file
            os.unlink(temp_audio.name)
            
            return {"text": result["text"]}
    except Exception as e:
        return {"error": str(e)}
