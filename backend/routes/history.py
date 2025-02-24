from fastapi import APIRouter
from backend.models.history import UserHistory
from backend.models.requests import TextRequest
from backend.database import history_collection
from backend.models.history import HistoryEntry
from datetime import datetime



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
def put_history(user_id: TextRequest, prompt: TextRequest, response: TextRequest):
    user_data = history_collection.find_one({"user_id": user_id.text})

    if not user_data:
        print(f"No user data was found for user_id [{user_id.text}]")  # Print actual requested user_id
        return {"error": "User not found"}
    
    new_history = [
        HistoryEntry(
            prompt=prompt.text, 
            response=response.text,
            timestamp=datetime.now()
        )
    ]

    user_data["history"].append(new_history[0].__dict__)  # Convert object to dictionary

    history_collection.update_one({"user_id": user_id.text}, {"$set": user_data})

    return {"message": "History entry added successfully."}