from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime

router = APIRouter()

client = MongoClient("mongodb+srv://baggiop1:PEBcap04!@cluster0.s8sih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["test_database"]
collection = db["tests"]

class TestRequest(BaseModel):
    text: str

@router.post("/", summary="Store a test")
async def create_test(request: TestRequest):
    test_entry = {"text": request.text, "timeSent": datetime.utcnow()}
    result = collection.insert_one(test_entry)
    if not result.inserted_id:
        raise HTTPException(status_code=500, detail="Failed to insert test")
    return {"test": request.text}

@router.get("/", summary="Fetch all tests")
async def get_tests():
    tests = list(collection.find({}, {"_id": 0, "text": 1, "timeSent": 1}))
    return {"tests": tests}
