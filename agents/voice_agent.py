# agents/voice_agent.py
import whisper
import pyttsx3

def speech_to_text(audio_file):
    model = whisper.load_model("base")
    return model.transcribe(audio_file)['text']

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
