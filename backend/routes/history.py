from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Text GET", description="Tests if the history router is working.")
def test():
    return {"message": "History Router Working"}