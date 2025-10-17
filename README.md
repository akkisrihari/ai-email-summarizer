# AI Email Summarizer

Summarize, extract actions & deadlines, generate smart replies, and set action reminders from any business email, PDF, or .eml file—all with a beautiful, fast web app.  
**No API keys required. Free, private, and fully offline using open-source AI!**

---

## Features

- **English Email Summarization** (BART transformer)
- **PDF and EML Upload:** Instantly extract & summarize whole emails from file
- **Action Item and Deadline Extraction:** See clear bullet points for tasks & dates
- **Automated Action Reminders:** Click a button to “set” reminders for any detected action or due date (pop-up/in-app for demo)
- **Smart Reply Generator:** Instant professional reply suggestion for every email
- **Text-to-Speech:** Listen to your summary aloud
- **Modern UI:** Light/dark mode, color theming, mobile-friendly

---

## Example Usage

- Paste any office/team email or upload a `.pdf` or `.eml` file
- Click **Summarize** for auto-extraction of summary, actions, and deadlines
- Click “Set Reminder” next to any action item/date (demo alert)
- See an auto-generated smart reply, ready to copy-paste!
- You can listen to the summary with audio output

---

## Setup Instructions

### 1. Clone and Install

git clone https://github.com/yourusername/ai-email-summarizer.git
cd ai-email-summarizer
python -m venv venv

Windows:
.\venv\Scripts\Activate.ps1

OR (for CMD)
.\venv\Scripts\activate.bat
pip install -r requirements.txt

text

### 2. Run the App

uvicorn app.main:app --reload

text
Then go to [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## Tech Stack

- Python 3.8+
- FastAPI backend
- Hugging Face Transformers (BART summarization)
- gTTS for text-to-speech
- pdfplumber for PDF extraction
- Jinja2 for HTML templates

---

## Project Structure

ai_email_summarizer/
├── app/
│ ├── init.py
│ ├── main.py
│ ├── summarize.py
│ └── templates/
│ └── index.html
├── requirements.txt
└── README.md

text

---

## Credits

Built by [Your Name] using modern open-source AI, for interviews, real-world workflow, and next-gen productivity.
