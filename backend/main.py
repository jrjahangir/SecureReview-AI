from fastapi import FastAPI
from datetime import datetime

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