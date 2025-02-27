# -AI-Powered-Career-Mentor-
  AI-Powered Career Mentor 
# AI-Powered Career Mentor

An intelligent career guidance system that combines the power of Google's Gemini AI, OpenAI's Whisper, and Coursera's learning recommendations.

## Features

- 🤖 Real-time AI career guidance using Google Gemini
- 🎤 Voice input support with Whisper API
- 📚 Personalized course recommendations from Coursera
- 👤 User profiles and chat history
- 🌐 Modern React frontend with FastAPI backend

## Tech Stack

- Frontend: React
- Backend: FastAPI
- Database: SQLite
- AI: Google Gemini API, Whisper API
- Learning Resources: Coursera API

## Setup

1. Clone the repository
```bash
git clone https://github.com/DevHoji/-AI-Powered-Career-Mentor-.git
cd AI-Powered-Career-Mentor
```

2. Install backend dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. Run the backend
```bash
cd backend
uvicorn main:app --reload
```

5. Install and run frontend
```bash
cd frontend
npm install
npm start
```

## Deployment

- Backend: Railway
- Frontend: Vercel

## API Documentation

Once the server is running, visit `/docs` for the interactive API documentation.
