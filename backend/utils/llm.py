
import os
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

# Locate .env in the project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

load_dotenv(PROJECT_ROOT / ".env")


def get_llm():

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Please configure it in the project root .env file."
        )

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    return model
