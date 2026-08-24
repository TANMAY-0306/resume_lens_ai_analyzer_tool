import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

try:
    import streamlit as st

    if not my_api_key:
        my_api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

if not my_api_key:
    raise ValueError("No API key found")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"

SUPPORTED_EXTENSIONS = (".pdf", ".docx")

MAX_FILE_SIZE = 5 * 1024 * 1024