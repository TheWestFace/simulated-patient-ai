import os
from dotenv import load_dotenv
from patient.gemini_config import configure_gemini

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = configure_gemini(api_key)


def load_prompt():

    with open("src/prompts/depression.txt") as f:
        return f.read()


SYSTEM_PROMPT = load_prompt()


def get_patient_response(user_text):

    full_prompt = SYSTEM_PROMPT + "\nClinician: " + user_text

    response = model.generate_content(full_prompt)

    return response.text
