# 1.Import Libraries.
import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv


# 2.Environment and Model Setup
load_dotenv()                                               ## Load environment variables from .env file
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

llm_text = genai.GenerativeModel("gemini-pro")              ## "gemini-pro" model, which is likely designed for text-based interactions like question answering.
llm_image = genai.GenerativeModel("gemini-pro-vision")      ## "gemini-pro-vision" model, which presumably handles image-based tasks like image captioning or understanding visual content.


# 3.Function Definitions
## for QA Bot
def text(question):
    text_response = llm_text.generate_content(question)
    return text_response.text


## For image
def image(input, image_file):
    if input!="":
        response = llm_image.generate_content([input,image_file])
    else:
        response = llm_image.generate_content(image_file)   
    return response.text

       