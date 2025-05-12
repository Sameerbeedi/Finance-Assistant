from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Optional
import os

# Import your agent modules
from agents import voice_agent, language_agent, retriever_agent

app = FastAPI(title="Voice Assistant API", 
              description="An API for processing audio and generating responses")

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint that returns API information"""
    return {
        "message": "Voice Assistant API",
        "endpoints": {
            "/brief": "POST endpoint for generating briefs from audio input",
            "/health": "GET endpoint for checking API health"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/brief")
async def generate_brief(audio_file: UploadFile = File(...), 
                         context_id: Optional[str] = None):
    """
    Process audio file and generate a brief summary response
    
    Args:
        audio_file: The audio file containing speech to process
        context_id: Optional context identifier for conversation history
    """
    try:
        # Read audio bytes
        audio_content = await audio_file.read()
        
        # Convert speech to text
        text = voice_agent.speech_to_text(audio_content)
        
        # Retrieve relevant data based on the text query
        retrieved_data = retriever_agent.retrieve_data(text, context_id)
        
        # Generate summary using language model
        summary = language_agent.generate_summary(text, retrieved_data)
        
        # Convert summary to speech
        audio_response = voice_agent.text_to_speech(summary)
        
        # Optional: Save audio response to file
        # response_path = f"responses/{context_id or 'default'}.mp3"
        # with open(response_path, "wb") as f:
        #     f.write(audio_response)
        
        return {
            "text_query": text,
            "response": summary,
            "audio_available": True
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/audio/{context_id}")
async def get_audio_response(context_id: str):
    """
    Get the audio response for a specific context
    
    Args:
        context_id: The context identifier
    """
    response_path = f"responses/{context_id}.mp3"
    
    if not os.path.exists(response_path):
        raise HTTPException(status_code=404, detail="Audio response not found")
    
    return FileResponse(
        response_path, 
        media_type="audio/mpeg", 
        filename=f"{context_id}.mp3"
    )

if __name__ == "__main__":
    # Create responses directory if it doesn't exist
    os.makedirs("responses", exist_ok=True)
    
    # Run the FastAPI app using Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")