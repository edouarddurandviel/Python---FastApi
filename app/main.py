from fastapi import FastAPI
from app.api.v1.user import router as user_router


app = FastAPI(title="first application")
app.include_router(user_router)
