from transformers import pipeline
import re
import random

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    result = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return result[0]['summary_text']

def extract_action_items(text):
    patterns = [
        r"\bplease.*?\.", r"\bupdate.*?\.", r"\bnotify.*?\.", r"\breview.*?\.", r"\bsubmit.*?\.", r"action required.*?\.", r"must.*?\.",
        r"\ballocate.*?\.", r"\bcontact.*?\.", r"\bresponsible.*?\.", r"\bfinish.*?\.", r"\bshare.*?\."
    ]
    found = []
    for pat in patterns:
        found += re.findall(pat, text, flags=re.IGNORECASE | re.DOTALL)
    return found

def extract_dates(text):
    date_pattern = r"(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday|next week|next (\w+)|\bEOD\b|\bCOB\b|(?:\d{1,2}/\d{1,2}/\d{2,4}))"
    return [m[0] for m in re.findall(date_pattern, text, flags=re.IGNORECASE)]

def generate_reply(summary):
    polite_replies = [
        "Thank you for your detailed email. Here’s my response:\n",
        "I appreciate your updates. Please see my feedback below:\n",
        "Thank you for bringing this to my attention. My response is as follows:\n"
    ]
    if "submit" in summary or "deadline" in summary or "by" in summary:
        body = "I have noted the deadlines and action items, and will complete them as requested.\n"
    else:
        body = "I understand the information provided, and will get back to you if further clarification is needed.\n"
    return random.choice(polite_replies) + body + "\nBest regards,\n[Your Name]"
