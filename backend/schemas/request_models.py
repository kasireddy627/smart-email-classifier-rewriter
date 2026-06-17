from pydantic import BaseModel

class EmailRequest(BaseModel):
    email: str

class RewriteRequest(BaseModel):
    email: str
    tone: str