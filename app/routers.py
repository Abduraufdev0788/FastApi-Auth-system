
from fastapi import APIRouter

from .schemas import UserCreate


router = APIRouter(prefix="/auth", tags=["Auth points"])

@router.post("/register")
async def register_api(user : UserCreate):
    pass