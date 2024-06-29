# 1.Import Statement
import streamlit as st
import google.generativeai as genai         ##  Imports the generativeai module from the google library. This module likely provides access to Google's generative AI models, including potentially Gemini.
from helper import get_gemini_response


# 2.Streamlit App Initialization:
st.set_page_config("GEMINI DEMO")
st.header("QA GEMINI DEMO")


# 3.User Input
input = st.text_input("Input: ", key = "input")
submit = st.button("Ask Question.")


# 4.Processing and Output
if submit:
    response = get_gemini_response(input)
    st.subheader("Thhe Answer Is")
    st.write(response)
