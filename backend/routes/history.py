from fastapi import APIRouter
from backend.models.history import UserHistory
from backend.models.requests import TextRequest
from backend.database import history_collection
from backend.models.history import HistoryEntry

router = APIRouter()

# POST route for getting someone's entire history of promts and responses
@router.post("/", summary="Getting history", description="Returns history of prompts, responses, and timestamps for specified user.")
def get_user_history(request: TextRequest):
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

# Need a way to PUT a JSON object as a history object for a specific user
# Adds a historyEntry to the history list for a specific user_id
@router.put("/", summary="Putting history for a user", description="Puts a new history entry for a specific user.")
def put_history(request: TextRequest):
    user_data = history_collection.find_one({"user_id": request.text})

    if not user_data:
        print(f"No user data was found for user_id [{request.text}]")  # Print actual requested user_id
        return {"error": "User not found"}

    history_entry = HistoryEntry(
        prompt = UserHistory.history[-1].prompt,
        response = UserHistory.history[-1].response,
        timestamp = datetime.utcnow()
    )

    if user_id in user_histories:
        user_histories[user_id].history.append(history_entry)
    else:
        # If the user doesn't have history yet, create a new entry
        user_histories[user_id] = UserHistory(user_id=user_id, history=[history_entry])
    
    return {
        "message": "History entry added successfully", 
        "user_id": user_id, 
        "entry": history_entry
    }