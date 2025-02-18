from fastapi import APIRouter
from backend.models.requests import TextRequest
router = APIRouter()

@router.post("/text", summary="Prompt LLM with text", description="Send a text prompt to the LLM and receive the LLMs response.")
def test(request: TextRequest):
    # TODO: Send text to the LLM and return the response
    return {"received_text": request.text}