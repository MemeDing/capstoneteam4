from fastapi import APIRouter
from backend.models.requests import TextRequest

router = APIRouter()

@router.get("/", summary="Health Check", description="Returns blank message as a health check tool.")
def health_check():
    return

@router.post("/text", summary="Prompt LLM with text", description="Send a text prompt to the LLM and receive the LLMs response.", response_model=TextRequest)
def text(request: TextRequest):
    # TODO: Send text to the LLM and return the response
    return {"text": request.text}