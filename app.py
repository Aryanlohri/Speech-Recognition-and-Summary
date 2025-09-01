from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from pydub import AudioSegment
import tempfile
import speech_recognition as sr
import os

# Initialize FastAPI
app = FastAPI(title="Speech Recognition & Summarization API")

# Load summarizer once
summarizer = pipeline(
    "summarization", 
    model="facebook/bart-large-cnn", 
    framework="pt", 
    device=-1
)

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Replace "*" with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health/")
async def health_check():
    """Simple health check endpoint"""
    return {"status": "ok", "message": "API is running"}

@app.post("/transcribe_and_summarize/")
async def transcribe_and_summarize(file: UploadFile = File(...)):
    """
    Accepts an audio file (wav, mp3, webm etc.), transcribes it using Google Speech API,
    and summarizes the text with HuggingFace transformers.
    """

    # Save uploaded file to a temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    # Convert to wav using pydub
    wav_path = tmp_path + ".wav"
    try:
        audio = AudioSegment.from_file(tmp_path)
        audio.export(wav_path, format="wav")
    except Exception as e:
        return JSONResponse({"error": f"Audio conversion failed: {e}"}, status_code=400)

    # Recognize speech
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 5
    recognizer.pause_threshold = 0.5
    recognizer.dynamic_energy_threshold = False

    try:
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    except Exception as e:
        return JSONResponse({"error": f"Speech recognition failed: {e}"}, status_code=400)
    finally:
        os.remove(tmp_path)
        if os.path.exists(wav_path):
            os.remove(wav_path)

    # Summarization
    summary = ""
    if len(text.split()) > 5:
        try:
            summary = summarizer(text, max_length=50, min_length=10, do_sample=False)[0]['summary_text']
        except Exception as e:
            summary = f"Summarization failed: {e}"

    return {"transcription": text, "summary": summary}

@app.post("/summarize_text/")
async def summarize_text(payload: dict):
    """
    Accepts raw text and returns its summary.
    Useful for manual input from frontend.
    """
    print("Received payload:", payload)  # Add this line for debugging
    text = payload.get("text", "")
    if not text:
        return JSONResponse({"error": "No text provided"}, status_code=400)

    summary = ""
    if len(text.split()) > 5:
        try:
            summary = summarizer(
                text, 
                max_length=50, 
                min_length=10, 
                do_sample=False
            )[0]['summary_text']
        except Exception as e:
            summary = f"Summarization failed: {e}"

    return {"summary": summary}
