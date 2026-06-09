from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from resume_parser import parse_resume
from interview_engine import generate_questions, evaluate_answer
import shutil
import os
from fastapi.responses import HTMLResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Temporary storage
sessions = {}

class AnswerRequest(BaseModel):
    session_id: str
    question: str
    answer: str

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    
    # Save file temporarily
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    # Parse resume
    resume_text = parse_resume(file_path)
    os.remove(file_path)
    
    # Generate questions
    questions = generate_questions(resume_text)
    
    # Create session
    session_id = f"session_{len(sessions)+1}"
    sessions[session_id] = {
        "resume": resume_text,
        "questions": questions,
        "current_q": 0,
        "scores": []
    }
    
    return {
        "session_id": session_id,
        "first_question": questions[0] if questions else "Tell me about yourself",
        "total_questions": len(questions)
    }

@app.post("/evaluate")
async def evaluate(req: AnswerRequest):

    session = sessions.get(req.session_id)
    if not session:
        return {"error": "Session not found"}

    result = evaluate_answer(
        req.question,
        req.answer,
        session["resume"]
    )

    session["scores"].append(result["score"])
    session["current_q"] += 1

    next_q = None
    is_complete = False
    ask_continue = False

    if session["current_q"] < len(session["questions"]):
        next_q = session["questions"][session["current_q"]]
    elif session["current_q"] == len(session["questions"]):
        # finished 10 questions — ask if continue or stop
        ask_continue = True
    else:
        is_complete = True

    final_score = None
    if is_complete:
        final_score = round(
            sum(session["scores"]) / len(session["scores"]), 1
        )

    return {
        "score": result["score"],
        "feedback": result["feedback"],
        "better_answer": result["better_answer"],
        "next_question": next_q,
        "is_complete": is_complete,
        "ask_continue": ask_continue,
        "final_score": final_score
    }

class ContinueRequest(BaseModel):
    session_id: str

@app.post("/continue-interview")
async def continue_interview(req: ContinueRequest):
    session = sessions.get(req.session_id)
    if not session:
        return {"error": "Session not found"}

    # Generate 5 more questions
    new_questions = generate_questions(session["resume"])
    session["questions"].extend(new_questions[:5])

    next_q = session["questions"][session["current_q"]]

    return {
        "next_question": next_q,
        "total_questions": len(session["questions"])
    }

@app.get("/")
async def serve_frontend():
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read())