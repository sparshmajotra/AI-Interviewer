# AI-Interviewer
AI-powered Interview Copilot that analyzes resumes, generates personalized technical interview questions, evaluates responses, and provides detailed feedback with scoring. Built with FastAPI, Groq LLaMA 3.3, and modern AI workflows.

# 🎯 AI Interview Copilot

<div align="center">

![AI Interview Copilot](https://img.shields.io/badge/AI-Interview%20Copilot-3b82f6?style=for-the-badge&logo=robot&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLaMA%203.3-FF6B35?style=for-the-badge&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)

**An AI-powered mock interview system that analyzes your resume, generates personalized technical questions, evaluates your answers, and gives detailed feedback — completely free.**

[🚀 Live Demo](#) · [📖 Documentation](#how-it-works) · [🐛 Report Bug](https://github.com/sparshmajotra/AI-interview-copilot/issues)

</div>

---

## 📸 Preview

```
Upload Resume → AI Generates Questions → Answer → Get Score + Feedback → Repeat
```

> Dark themed UI with animated car drift loader, live score tracking, progress indicators, and confetti on great scores 🎉

---

## ✨ Features

- 📄 **Resume Analysis** — Upload your PDF resume, AI reads and understands your skills
- 🤖 **Personalized Questions** — 10 technical questions generated specifically from your resume
- 💬 **Real-time Evaluation** — AI evaluates every answer with a score out of 10
- 📊 **Detailed Feedback** — What you did well, what was missing, and a model answer
- 🔄 **Infinite Loop Mode** — After 10 questions, choose to continue with 5 more or end
- 🏆 **Final Score Report** — Overall performance score with badges and assessment
- 🎨 **Dark UI + Animations** — Car drift loader, progress bars, confetti on high scores
- 💰 **100% Free** — Uses Groq's free API tier, no credit card required

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, FastAPI |
| **AI Model** | Groq API — LLaMA 3.3 70B (free tier) |
| **PDF Parsing** | pdfplumber |
| **Frontend** | HTML, CSS, Vanilla JavaScript |
| **Deployment** | Render (free tier) |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Free Groq API key → [console.groq.com](https://console.groq.com)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/sparshmajotra/AI-interview-copilot.git
cd AI-interview-copilot
```

**2. Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your free key at → [console.groq.com](https://console.groq.com) (no credit card needed)

**5. Run the application**
```bash
uvicorn main:app --reload
```

**6. Open in browser**
```
http://localhost:8000
```

---

## 📁 Project Structure

```
AI-interview-copilot/
│
├── main.py                 # FastAPI backend — routes and session management
├── interview_engine.py     # AI logic — question generation and answer evaluation
├── resume_parser.py        # PDF parsing — extracts text from uploaded resume
├── index.html              # Frontend — dark UI with animations
├── requirements.txt        # Python dependencies
├── .env                    # API keys (not committed)
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   1. User uploads PDF resume                        │
│          ↓                                          │
│   2. pdfplumber extracts text from PDF              │
│          ↓                                          │
│   3. Groq LLaMA 3.3 generates 10 personalized      │
│      technical interview questions                  │
│          ↓                                          │
│   4. User answers each question in the chat UI     │
│          ↓                                          │
│   5. AI evaluates answer → Score (0-10)            │
│      + Feedback + Better answer suggestion          │
│          ↓                                          │
│   6. After 10 questions → Continue or End          │
│          ↓                                          │
│   7. Final score + performance badges              │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/upload-resume` | Upload PDF, parse resume, generate 10 questions |
| `POST` | `/evaluate` | Submit answer, get score + feedback + next question |
| `POST` | `/continue-interview` | Generate 5 more questions after round completion |
| `GET` | `/` | Serve the frontend HTML |

### Request/Response Examples

**POST /upload-resume**
```json
// Response
{
  "session_id": "session_1",
  "first_question": "Explain how Django handles a request-response cycle.",
  "total_questions": 10
}
```

**POST /evaluate**
```json
// Request
{
  "session_id": "session_1",
  "question": "Explain how Django handles a request-response cycle.",
  "answer": "Django uses URL routing to match the request..."
}

// Response
{
  "score": 8,
  "feedback": "Good explanation of URL routing and views...",
  "better_answer": "A complete answer would also mention middleware...",
  "next_question": "What is the difference between Django ORM and raw SQL?",
  "is_complete": false,
  "ask_continue": false,
  "final_score": null
}
```

---

## 🌐 Deployment on Render (Free)

1. Push code to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repository
4. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variable:
   - `GROQ_API_KEY` → your Groq API key
6. Click **Deploy** → Live in 2 minutes ✅

---

## 💡 Use Cases

- 🎓 **Students** — Practice before campus placements
- 💼 **Job Seekers** — Prepare for technical interviews
- 🔄 **Career Switchers** — Build confidence in new tech domains
- 🏢 **Coaching Institutes** — Integrate as a practice tool for students

---

## 🗺️ Roadmap

- [ ] Voice answer support (speak instead of type)
- [ ] Multiple interview modes (HR, Technical, System Design)
- [ ] Answer history and progress tracking
- [ ] Export interview report as PDF
- [ ] Multi-language support (Hindi + English)
- [ ] Company-specific interview modes (Google, Amazon, etc.)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repo
2. Create your branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 👨‍💻 Author

**Sparsh Majotra**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-sparshmajotra-0077B5?style=flat&logo=linkedin)](https://linkedin.com/in/sparshmajotra)
[![GitHub](https://img.shields.io/badge/GitHub-sparshmajotra-181717?style=flat&logo=github)](https://github.com/sparshmajotra)

---

<div align="center">

**If this project helped you, please give it a ⭐ — it means a lot!**

Made with ❤️ by Sparsh Majotra

</div>