from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
 
from app.core import config
from app.core.database import init_pg_db
from app.services.battleship.battleship_router import router as battleship_router

 
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
    print("View The Docs On : http://127.0.0.1:8000/docs")

@app.get('/')
async def health_check():
    return {
        'message' : 'Welcome To Python Project'
    }  

@app.get('/heath-check')
async def health_check():
    return {
        'status' : 'ok'
    }


app.include_router(battleship_router)