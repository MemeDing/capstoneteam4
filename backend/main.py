from fastapi import FastAPI
from backend.routes import history, prompt

app = FastAPI(title="Improving Intelligence Confidence")

# Include Routers
app.include_router(prompt.router, prefix="/prompt", tags=["prompt"])
app.include_router(history.router, prefix="/history", tags=["history"])