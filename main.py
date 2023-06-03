from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.api import router as api_router
import os

app = FastAPI()

origins = ["http://localhost:5000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


IMAGE_STORE_PATH = os.path.abspath("./src/store")

if not os.path.exists(IMAGE_STORE_PATH):
    os.makedirs(IMAGE_STORE_PATH)

app.include_router(api_router)
