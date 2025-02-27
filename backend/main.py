from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from init_db import init_database

# Load environment variables
load_dotenv()

# Initialize database
init_database()

app = FastAPI(title="AI Career Mentor API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to AI Career Mentor API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
