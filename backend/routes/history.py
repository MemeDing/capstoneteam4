from fastapi import APIRouter
from backend.models.history import UserHistory

router = APIRouter()

@router.get("/", summary="Health Check", description="Returns blank message as a health check tool.")
def health_check():
    return

# GET route for getting someone's entire history of promts and responses
@router.get("/history", summary="Getting history", description="Returns history of prompts, responses, and timestamps for specified user.")
def get_history(user_id: str):
    user_data = history_collection.find_one({"user_id": user_id})

    if not user_data:
        print(f"No user data was found for user_id [{user_data}]")
        return

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

# POST route for posting new prompts