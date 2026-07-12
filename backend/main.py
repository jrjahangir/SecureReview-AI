from fastapi import FastAPI, File, UploadFile
from datetime import datetime
import os
import uuid
from backend.app.models.request_models import CodeReviewRequest
from backend.app.security.validator import ( 
        validate_extension, 
        validate_file_size,
        )
from backend.app.security.hashing import calculate_sha256
from backend.app.analyzer.codeanalyzer import analyze_source_code
from backend.app.analyzer.risk_engine import calculate_risk
from backend.app.ai.aiservice import analyze_with_ai
from backend.app.report.report_generator import generate_report

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

    extension = validate_extension(file.filename)

    os.makedirs("uploads", exist_ok=True)

    unique_filename = f"{uuid.uuid4()}{extension}"

    file_path = os.path.join("uploads", unique_filename)

    file_bytes = await file.read()

    validate_file_size(file_bytes)

    file_hash = calculate_sha256(file_bytes)

    with open(file_path, "wb") as buffer:
        buffer.write(file_bytes)

    source_code = file_bytes.decode("utf-8", errors="replace")

    findings = analyze_source_code(source_code)

    risk = calculate_risk(findings)

    ai_result = analyze_with_ai(source_code)

    report = generate_report(
        file.filename,
        file_hash,
        risk,
        findings,
        ai_result
    )

    return report
    
 #  return {
 #  "message": "File uploaded successfully",
 #  "original_filename": file.filename,
 #  "saved_filename": unique_filename,
 #  "content_type": file.content_type,
 #  "sha256": file_hash,
 #  "risk_score": risk["score"],
 #  "risk_level": risk["level"],
 #  "summary": risk["summary"],
 #  "findings": findings,
 # "ai_analysis": ai_result
 # } 