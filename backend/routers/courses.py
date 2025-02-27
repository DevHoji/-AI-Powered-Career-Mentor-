from fastapi import APIRouter, HTTPException
import os
import requests
from typing import List

router = APIRouter()

COURSERA_API_KEY = os.getenv("COURSERA_API_KEY")
COURSERA_API_URL = "https://api.coursera.org/api/courses.v1"

@router.get("/courses/{career_field}")
async def get_courses(career_field: str, limit: int = 5) -> List[dict]:
    try:
        params = {
            "q": career_field,
            "limit": limit,
            "fields": "name,description,photoUrl,partnerLogo"
        }
        headers = {
            "Authorization": f"Bearer {COURSERA_API_KEY}"
        }
        
        response = requests.get(COURSERA_API_URL, params=params, headers=headers)
        response.raise_for_status()
        
        courses = response.json().get("elements", [])
        return courses
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
