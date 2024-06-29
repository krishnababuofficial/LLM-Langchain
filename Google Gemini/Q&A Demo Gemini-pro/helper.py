# 1.Import Statement
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
## load_dotenv(): This function reads environment variables from a file named .env in the current working directory and loads them into the environment. 
## This is a common way to store sensitive information like API keys without hardcoding them in the script.


# 2.Configuring API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))            ##  The API key is retrieved from the environment variable GOOGLE_API_KEY using os.getenv()

## genai.configure()- The purpose of this function is to provide necessary configuration details for the module to work correctly.
## api_key parameter, which is essential for authentication and access to Google's AI services.
## os.getenv("GOOGLE_API_KEY"): This part retrieves the value of the environment variable named "GOOGLE_API_KEY".


# 3.Function to load gemini pro model
model = genai.GenerativeModel("gemini-pro")


# 4.Response 
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text