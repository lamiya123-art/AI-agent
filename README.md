# 🤖 TaskFlow AI — AI Powered Productivity Assistant

TaskFlow AI is an intelligent productivity assistant that uses **Google Gemini AI** and **Asana API** to convert natural language conversations into actionable tasks.  
The agent understands user requests, extracts task details, and automatically creates organized tasks inside an Asana workspace.

---

## 🚀 Features

- 💬 Natural language based task creation
- 🤖 Gemini AI powered conversational assistant
- 🔧 AI Function Calling / Tool Integration
- 📌 Automatic Asana task creation
- 📅 Intelligent due date handling
- 🔐 Secure API key management using environment variables
- ⚠️ Error handling for API failures and model availability
- 🧠 Maintains conversation flow

---

## 🛠️ Tech Stack

**Language**
- Python

**AI & APIs**
- Google Gemini API
- Asana API

**Tools & Libraries**
- google-genai
- asana-python-sdk
- python-dotenv
- JSON
- Git & GitHub

---

## 🧠 How It Works

```
User Input
    |
    ↓
Gemini AI Agent
    |
    ↓
Understands Intent
    |
    ↓
Function Calling
    |
    ↓
Asana API
    |
    ↓
Task Created Successfully
```

Example:

User:

```
Create a task called Finish DSA array problems due tomorrow
```

TaskFlow AI:

```
✅ Task created successfully

📌 Task: Finish DSA array problems
📅 Due Date: 2026-07-09
🔗 Added to Asana Workspace
```

---

## 📂 Project Structure

```
TaskFlow-AI
│
├── agents.py          # Main AI agent logic
├── .env               # API credentials
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/lamiya123-art/taskflow-ai.git

cd taskflow-ai
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key

ASANA_ACCESS_TOKEN=your_asana_access_token

ASANA_PROJECT_ID=your_asana_project_id
```

---

## ▶️ Run the Agent

```bash
python agents.py
```

Start chatting:

```
Chat with me(q to quit):
```

Example:

```
create a task called Complete ML assignment due tomorrow
```

---

## 📸 Demo

```
Chat with me: create a task called Finish DSA problems due tomorrow


✅ Task created successfully

Task: Finish DSA problems
Due Date: Tomorrow
Added successfully to Asana
```

---

## 📚 Concepts Implemented

- Large Language Model (LLM) Integration
- AI Agents
- Function Calling
- API Integration
- REST API Communication
- Environment Configuration
- Exception Handling
- Automation Workflow

---

## 🌱 Future Improvements

- Add voice assistant support
- Integrate Google Calendar
- Add email reminders
- Build a web dashboard
- Support multiple productivity tools

---

## 👩‍💻 Developer

**Lamiya Shuaib**

Computer Science Engineering Student  
Interested in Software Development, Artificial Intelligence, and Full Stack Development.

---

⭐ If you like this project, consider giving it a star!
