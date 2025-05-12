# 📊 Finance Assistant

**Finance Assistant** is a smart tool designed to provide financial market insights by converting audio briefs into written summaries, scraping relevant data, and offering an interactive UI for users. It uses **FastAPI** for backend services and **Streamlit** for the frontend interface.

---

## 🚀 Features

- 🎤 **Market Briefs**: Generate financial summaries directly from audio files.
- 🌐 **Web Scraping**: Retrieve real-time financial data and news using APIs.
- 🖥️ **Streamlit Interface**: User-friendly UI to upload files and view results.
- ⚙️ **FastAPI Backend**: Microservice architecture for audio and data processing.
- 🧠 **Whisper Integration**: Leverage OpenAI’s Whisper for speech-to-text processing.

---

## 🧰 Prerequisites

Make sure the following are installed:

- Python 3.8+
- `pip` (Python package manager)
- `ffmpeg` (required for Whisper STT)

---

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-repo/finance-assistant.git
   cd finance-assistant

2. **Install dependencies:**
    ```bash 
    pip install -r requirements.txt

3. **Install ffmpeg:**
    - For Windows: Download FFmpeg and add it to your PATH.
    - macOS:
    ```bash
    brew install ffmpeg
    ```
    - Linux:
    ```bash
    sudo apt update
    sudo apt install ffmpeg
    ```

## ▶️Usage
### 1. **Start the FastAPI Backend**
Run the server to handle audio processing and summaries:
```bash
    uvicorn orchestrator.orchestrator:app --reload
```
### 2. Test the API (Optional)
Use curl to test the /brief endpoint:
```bash
    curl -X POST http://127.0.0.1:8000/brief -F "audio_file=@input.wav"
```

### 3.Launch the Streamlit App
Start the frontend(replace the api endpoint) to upload files and view results:
```bash
    streamlit run app/app.py
```
## 📁 Project Structure 
finance-assistant/
│
├── app/                     # Streamlit frontend
│   └── app.py
│
├── data_ingestion/          # Data scraping and ingestion scripts
│   └── filings_scraper.py
│
├── orchestrator/            # FastAPI backend
│   └── orchestrator.py
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── input.wav                # Example audio file (optional)





    
