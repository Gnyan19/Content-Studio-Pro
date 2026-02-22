import os
from dotenv import load_dotenv
from google.genai import Client


def configure_model():
    load_dotenv()

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")

    return Client(api_key=api_key)