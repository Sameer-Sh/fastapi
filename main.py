from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
 
from app.core import config
from app.core.database import init_pg_db

 
app = FastAPI(**config.APP_CONFIGS)
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    init_pg_db(app)