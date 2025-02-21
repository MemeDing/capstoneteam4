from pydantic import BaseModel
from datetime import datetime
from typing import List

class HistoryEntry(BaseModel):
    prompt: str
    response: str
    timestamp: datetime

class UserHistory(BaseModel):
    user_id: str  # Assuming each user has a unique identifier
    history: List[HistoryEntry]
