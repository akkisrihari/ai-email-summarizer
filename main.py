from fastapi import FastAPI, Request, Form, UploadFile
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from app.summarize import summarize_text, extract_action_items, extract_dates, generate_reply
from gtts import gTTS
import pdfplumber
import email
from email import policy

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "summary": None,
            "actions": None,
            "dates": None,
            "reply": None,
            "email_text": ""
        }
    )

@app.post("/summarize", response_class=HTMLResponse)
async def summarize(request: Request, email_text: str = Form(...)):
    summary = summarize_text(email_text)
    actions = extract_action_items(email_text)
    dates = extract_dates(email_text)
    reply = generate_reply(summary)
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "summary": summary,
            "actions": actions,
            "dates": dates,
            "reply": reply,
            "email_text": email_text
        }
    )

@app.post("/speak")
async def speak(summary: str = Form(...)):
    tts = gTTS(summary)
    tts.save("summary.mp3")
    return FileResponse("summary.mp3", media_type="audio/mpeg", filename="summary.mp3")

@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file_type: str = Form(...), upload_file: UploadFile = Form(...)):
    content = ""
    if file_type == "pdf" and upload_file.filename.endswith('.pdf'):
        with pdfplumber.open(upload_file.file) as pdf:
            text = [page.extract_text() or "" for page in pdf.pages]
            content = "\n".join(text)
    elif file_type == "eml" and upload_file.filename.endswith('.eml'):
        raw_bytes = await upload_file.read()
        msg = email.message_from_bytes(raw_bytes, policy=policy.default)
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    content += part.get_payload(decode=True).decode(part.get_content_charset() or "utf-8")
        else:
            content = msg.get_payload(decode=True).decode(msg.get_content_charset() or "utf-8")
    else:
        content = "File type and extension do not match or not supported!"

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "summary": None,
            "actions": None,
            "dates": None,
            "reply": None,
            "email_text": content
        }
    )

