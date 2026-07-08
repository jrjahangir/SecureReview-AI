from fastapi import FastAPI
from fastapi import UploadFile, File
from fastapi import HTTPException
from pathlib import Path
from datetime import datetime
from backend.app.models.request_models import CodeReviewRequest
import os
import uuid

ALLOWED_EXTENSIONS = {
    ".java",
    ".py",
    ".php",
    ".js",
    ".cs",
    ".html",
    ".xml"
}
app = FastAPI(
    title="SecureReview-AI",
    version="0.1.0",
    description="AI-Powered Application Security Assessment Platform"
)

@app.get("/")
def root():
    return {
        "application": "SecureReview-AI",
        "version": "0.1.0",
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/about")
def about():
    return {
        "application": "SecureReview-AI",
        "developer": "Md. Jahangir Hossain",
        "purpose": "AI-Powered Security Assessment"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "SecureReview-AI API",
        "version": "0.1.0"
    }
@app.get("/developer")
def developer():
    return {
        "name": "Md. Jahangir Hossain",
        "role": "Cyber Security Professional",
        "current_project": "SecureReview-AI",
        "learning": [
            "Python",
            "FastAPI",
            "Docker",
            "Artificial Intelligence"
        ]
    }
@app.post("/review")
def review_code(request: CodeReviewRequest):
    return {
        "status": "received",
        "developer": request.developer,
        "language": request.language,
        "filename": request.filename,
        "message": "Source code received successfully."
    }
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"File type '{extension}' is not allowed."
        )

    os.makedirs("uploads", exist_ok=True)

    unique_filename = f"{uuid.uuid4()}{extension}"

    file_path = os.path.join("uploads", unique_filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "message": "File uploaded successfully",
        "original_filename": file.filename,
        "saved_filename": unique_filename,
        "content_type": file.content_type
    }