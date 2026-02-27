import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash-lite")

system_prompt = """You are a patient struggling with depression.
Speak in one sentence to describe how you're feeling."""

response = model.generate_content(system_prompt)

print(response.text)
