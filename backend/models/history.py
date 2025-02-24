from pydantic import BaseModel
from datetime import datetime
from typing import List

class HistoryEntry(BaseModel):
    prompt: str
    response: str
    timestamp: datetime

class UserHistory(BaseModel):
    user_id: str
    history: List[HistoryEntry]
