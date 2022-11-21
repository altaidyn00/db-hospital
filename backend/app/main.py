from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api import api
from app.engine import engine
from app.migration import create_tables

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    create_tables()
except Exception as e:
    print(e)
    

app.include_router(api.router, prefix="/api")