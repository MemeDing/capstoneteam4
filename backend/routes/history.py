from fastapi import APIRouter
from backend.models.history import UserHistory
from backend.models.requests import TextRequest
from backend.database import history_collection
from backend.models.history import HistoryEntry

router = APIRouter()

# POST route for getting someone's entire history of promts and responses
@router.post("/", summary="Getting history", description="Returns history of prompts, responses, and timestamps for specified user.")
def get_history(request: TextRequest):
    user_data = history_collection.find_one({"user_id": request.text})

    if not user_data:
        print(f"No user data was found for user_id [{request.text}]")  # Print actual requested user_id
        return {"error": "User not found"}

    # Convert MongoDB's timestamp format if necessary
    history = [
        HistoryEntry(
            prompt=entry["prompt"],
            response=entry["response"],
            timestamp=entry["timestamp"]
        )
        for entry in user_data.get("history", [])
    ]

    return UserHistory(user_id=user_data["user_id"], history=history)