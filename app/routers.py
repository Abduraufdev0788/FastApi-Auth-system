from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth points"])

@router.post("/register")
async def register_api():
    pass