# Conversationa Q&A Chatbot
# 1. Imports
import streamlit as st
from streamlit.commands import page_config          ## Imports functions for configuring the Streamlit page settings.
import helper


# 2. Page Configuration
st.set_page_config(page_title = "Conversational Q&A Chatbot.")      
## st.set_page_config: This function configures the Streamlit app's display settings, page_title: Sets the title that appears in the browser tab for the app.


# 3. Header and User Input
st.header("Hey Let's Chat")
input = st.text_input("Input: ", key="input")


# 4. Generating Response and Button
response = helper.get_chatmodel_response(input)
submit = st.button("Ask the question")


# 5. Displaying Response
if submit:                                      ## if ask button is clicked
    st.subheader("The Response is")
    st.write(response)
