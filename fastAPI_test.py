from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["testDB"]
collection = db["tests"]

# Define a test model
class Test(BaseModel):
    text: str

@app.post("/tests/")
async def create_test(test: Test):
    """Stores a test in MongoDB"""
    test_data = {
        "text": test.text,
        "timeSent": datetime.now()
    }
    collection.insert_one(test_data)
    return {"test": "Test stored successfully"}

@app.get("/tests/")
async def get_test():
    """Fetch all tests from MongoDB"""
    tests = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB's "_id"
    return {"tests": tests}
