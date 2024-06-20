# 1. Imports and Setup
from langchain_openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os


load_dotenv()   ## Loads environment variables from the .env file. Make sure your OpenAI API key is set as an environment variable named OPENAI_API_KEY in the .env file.

chat_llm = OpenAI(temperature = 0.3)        ## Temperature controls the randomness of the model's output; lower values make it more deterministic and focused.


# 2. Function to load OpenAI model and get response
def get_openai_response(question):
    llm = chat_llm
    response = llm(question)
    return response


# 3. Initialize streamlit Application Setup:
st.set_page_config(page_title="QA DEMO")                        ## Title of the Streamlit application tab 

st.header("Langchain Application")                              ## Header to the app saying "Langchain Application"

input = st.text_input("Input: ", key="input")                   ## User can type their question here. KEY- Unique Identifier: Each Streamlit widget requires a unique key. This key acts as an identifier, allowing Streamlit to distinguish between different input elements and track their individual states.
response = get_openai_response(input)                           ## Response from OpenAI for the input question

submit = st.button("Ask the question")                          


#4. Interaction and Response:
if submit:                                            ## If ask button is clicked.
    st.subheader("The Response is")
    st.write(response)