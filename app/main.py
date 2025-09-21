from fastapi import FastAPI

from .models import User, Task
from .database import Base, engine

app = FastAPI(title="Auth system")

Base.metadata.create_all(engine)

@app.get("/")
async def home():
    return {"message": "Auth system"}