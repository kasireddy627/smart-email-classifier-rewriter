from fastapi import FastAPI
from services.classifier_service import classify_email_service
from schemas.request_models import EmailRequest
from schemas.request_models import RewriteRequest
from services.rewriter_service import rewrite_email_service
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Smart Email AI is running"}

@app.post("/classify_email")
def classify_email(request: EmailRequest):
    return classify_email_service(request.email)


@app.post("/rewrite_email")
def rewrite_email(request: RewriteRequest):
    return rewrite_email_service(
        request.email,
        request.tone
    )