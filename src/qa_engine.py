import vertexai
vertexai.init(project="fintech-qa-llm-gemini", location="us-central1")
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv() # load environment variables (API KEY)
genai.configure(api_key=os.getenv("GEMINI_API_KEY")) # load API key

def gemini_generate(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)
    return(response.text)


def mock_generate(prompt):
    # use this function as a placeholder to avoid repeated api calls when testing unrelated functionality
    return("*Generated Response*")

