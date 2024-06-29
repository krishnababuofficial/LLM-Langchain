# 1.Import Libraries
import os                                       ## for interacting with the operating system, likely for accessing environment variables.
import google.generativeai as genai
import streamlit as st
from PIL import Image                          ## Pillow (PIL) library for handling image processing tasks.
from dotenv import load_dotenv
load_dotenv()       ## Loads environment variables from the .env file.


# 2.Environment and Model Set.
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))        ## Configures the genai module with the Google API key obtained from the environment.

model = genai.GenerativeModel("gemini-pro-vision")          ## "gemini-pro-vision" model, which likely supports image processing


# 3.Create get_gemini_response Function:
def get_gemini_response(input,image):                       
    if input!="":                                                 ## Checks if there is any textual input provided.
        response = model.generate_content([input,image])          ## If there is input, it calls model.generate_content([input, image]), passing both the text and image to the model for generating content
    else:
        response = model.generate_content(image)                  ##  If there is no text input, it calls model.generate_content(image), providing only the image to the model.
    return response.text                                          ## Returns the generated text response from the model.


# 4.Streamlit App Initialization
st.set_page_config("GEMINI IMAGE DEMO")
st.header("QA IMAGE GEMINI DEMO")

input = st.text_input("Input: ", key = "input")


upload_file = st.file_uploader("Choose an image...", type = ["jpg", "jpeg", "png"])             ## Creates a file uploader widget allowing users to upload image files of specified types.
image = ""                                                                                    ## Initializes an empty variable to store the image object.

# 5.Image Processing.
if upload_file is not None:                                                     ## Check if image as been Uploaded.
    image = Image.open(upload_file)                                             ## Using the PIL open the image file  and store itin image.
    st.image(image, caption = "Uploaded Imges.", use_column_width=True)         ## Displays the uploaded image in the app using Streamlit's st.image function.

# 5.User Interaction and Response.
submit= st.button("Tell Me About The Image")        

if submit:                                                  ## when submit button is clicked
    response = get_gemini_response(input, image)
    st.subheader("The Response Is")
    st.write(response)
