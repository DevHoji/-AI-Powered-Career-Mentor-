from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import google.generativeai as genai
from ..database import get_db
from ..models import ChatHistory
import os

router = APIRouter()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

@router.post("/chat")
async def chat_with_ai(message: str, user_id: int, db: Session = Depends(get_db)):
    try:
        # Generate AI response using Gemini
        response = model.generate_content(message)
        
        # Save chat history
        chat_entry = ChatHistory(
            user_id=user_id,
            query=message,
            response=response.text
        )
        db.add(chat_entry)
        db.commit()
        
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
