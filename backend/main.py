from fastapi import FastAPI
from backend.routes import history, prompt, tests
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient

app = FastAPI(title="Improving Intelligence Confidence")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")

# MongoDB connection
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://baggiop1:PEBcap04!@cluster0.s8sih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Include Routers
app.include_router(prompt.router, prefix="/prompt", tags=["prompt"])
app.include_router(history.router, prefix="/history", tags=["history"])
app.include_router(tests.router, prefix="/tests", tags=["tests"])