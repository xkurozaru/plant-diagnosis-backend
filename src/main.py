from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.interface.prediction import prediction_router
from src.interface.user import account_router

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes
app.include_router(account_router.router)
app.include_router(prediction_router.router)
