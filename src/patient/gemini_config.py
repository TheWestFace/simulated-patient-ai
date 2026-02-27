import google.generativeai as genai


def configure_gemini(api_key):

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-pro")

    return model
