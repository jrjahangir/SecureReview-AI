from pathlib import Path
from fastapi import HTTPException

ALLOWED_EXTENSIONS = {
    ".java",
    ".py",
    ".php",
    ".js",
    ".cs",
    ".html",
    ".xml"
}

def validate_extension(filename: str):

    extension = Path(filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"File type '{extension}' is not allowed."
        )

    return extension