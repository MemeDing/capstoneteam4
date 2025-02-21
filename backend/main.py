from fastapi import FastAPI
from backend.routes import history, prompt
from backend.database import client

app = FastAPI(title="Improving Intelligence Confidence")

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Include Routers
app.include_router(prompt.router, prefix="/prompt", tags=["prompt"])
app.include_router(history.router, prefix="/history", tags=["history"])