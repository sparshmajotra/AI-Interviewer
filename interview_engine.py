from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_questions(resume_text: str) -> list:
    prompt = f"""
    Based on this resume, generate 5 technical 
    interview questions. Mix easy and hard.
    Return as numbered list only.
    
    Resume:
    {resume_text[:2000]}
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500
    )
    
    raw = response.choices[0].message.content
    questions = [q.strip() for q in raw.split('\n') 
                 if q.strip() and q[0].isdigit()]
    return questions

def evaluate_answer(
    question: str, 
    answer: str, 
    resume_text: str
) -> dict:
    prompt = f"""
    You are an expert technical interviewer.
    
    Question: {question}
    Candidate Answer: {answer}
    Candidate Background: {resume_text[:500]}
    
    Evaluate the answer and respond in this 
    exact format:
    
    SCORE: [0-10]
    FEEDBACK: [2-3 lines of honest feedback]
    BETTER_ANSWER: [What a great answer looks like]
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400
    )
    
    raw = response.choices[0].message.content
    
    score = 5
    feedback = ""
    better = ""
    
    for line in raw.split('\n'):
        if line.startswith('SCORE:'):
            try:
                score = int(line.split(':')[1].strip())
            except:
                score = 5
        elif line.startswith('FEEDBACK:'):
            feedback = line.replace('FEEDBACK:', '').strip()
        elif line.startswith('BETTER_ANSWER:'):
            better = line.replace('BETTER_ANSWER:', '').strip()
    
    return {
        "score": score,
        "feedback": feedback,
        "better_answer": better
    }