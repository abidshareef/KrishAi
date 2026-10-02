"""Local API contract for the KrishiAI prototype."""

from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="KrishiAI Prototype API", version="0.1.0")

class DiagnoseRequest(BaseModel):
    user_id: str = Field(min_length=1)
    crop: str | None = None
    image_url: str | None = None
    voice_text: str | None = None
    language: str = "en"

class FeedbackRequest(BaseModel):
    user_id: str = Field(min_length=1)
    request_id: str = Field(min_length=1)
    rating: int = Field(ge=1, le=5)
    comment: str | None = None

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "krishiai-api"}

@app.post("/diagnose")
def diagnose(request: DiagnoseRequest) -> dict[str, Any]:
    request_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    return {
        "request_id": request_id,
        "status": "prototype",
        "message": "Input accepted; connect a validated vision model and knowledge layer.",
        "input": request.model_dump(),
        "confidence": None,
    }

@app.post("/voice-query")
def voice_query(request: DiagnoseRequest) -> dict[str, Any]:
    return {"status": "prototype", "message": "Connect Amazon Transcribe for audio input.", "language": request.language, "text": request.voice_text}

@app.get("/history/{user_id}")
def history(user_id: str) -> dict[str, Any]:
    return {"user_id": user_id, "items": []}

@app.post("/feedback")
def feedback(request: FeedbackRequest) -> dict[str, Any]:
    return {"status": "accepted", "feedback": request.model_dump()}
