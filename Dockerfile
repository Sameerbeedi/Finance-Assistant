# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default FastAPI command (can be overridden)
CMD ["uvicorn", "orchestrator.orchestrator:app", "--host", "0.0.0.0", "--port", "8000"]
