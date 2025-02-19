from fastapi import APIRouter
from backend.models.history import UserHistory

router = APIRouter()

@router.get("/", summary="Health Check", description="Returns blank message as a health check tool.")
def health_check():
    return

# GET route for getting someone's entire history of promts and responses
@router.get("/history", summary="Getting history", description="Returns history of prompts, responses, and timestamps for specified user.")
def get_history():
    return {user_id }

# POST route for posting new prompts