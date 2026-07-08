from pydantic import BaseModel
class CodeReviewRequest(BaseModel):
    developer: str
    language: str
    filename: str
    code: str