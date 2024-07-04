# 1.Import Libraries
import streamlit as st
import google.generativeai as genai
import os
from PIL import Image                   ## PIL.Image: Imports the Python Imaging Library (PIL) for working with images.
from dotenv import load_dotenv
import helper

load_dotenv()

# 2.Q&A Bot Interface:
## initialize our streamlit for QA
st.set_page_config("GEMINI DEMO QA-BOT & IMAGE-TO-TEXT")
st.header("QA-BOT GEMINI DEMO")

input_QABot = st.text_input("Input: ", key = "text_input")
submit_QABot = st.button("Ask Question.")


# when submit button is clicked

if submit_QABot:
    response = helper.text(input_QABot)
    st.subheader("The Answer Is")
    st.write(response)


## initialize our streamlit for IMAGE-TO-TEXT

st.header("IMAGE-TO-TEXT GEMINI DEMO")

upload_file = st.file_uploader("Choose an image...", type = ["jpg", "jpeg", "png"])
image = ""
if upload_file is not None:
    image = Image.open(upload_file)
    st.image(image, caption = "Uploaded Imges.", use_column_width=True)

input_img = st.text_input("Input: ", key = "image_input")
submit_img= st.button("Tell Me About The Image")


# when submit button is clicked

if submit_img:
    response_img = helper.image(input_img, image)
    st.subheader("The Response Is")
    st.write(response_img)



