from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Health Check", description="Returns blank message as a health check tool.")
def health_check():
    return