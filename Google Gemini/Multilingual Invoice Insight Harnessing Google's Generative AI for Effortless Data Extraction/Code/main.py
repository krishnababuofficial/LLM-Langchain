# 1. Setup and Imports.

# Create VirtualEnvironment: "conda create -p venv python==3.10"
# Activate Conda: "conda activate venv/"
# Pip install -r requirements.txt
## Environment Setup:  The initial commented lines suggest setting up a virtual environment using conda and installing dependencies from a requirements.txt file.

## Imports:
import os
from dotenv import load_dotenv
load_dotenv()                                               ## Load all environment variable from .env

import streamlit as st
import google.generativeai as GenAi
from PIL import Image            
import helper

## Page Configuration:
st.set_page_config(page_title="MultiLanguage Invoice Extractor")
st.header("MultiLanguage Invoice Extractor")


# 2. User Input.
upload_file = st.file_uploader("Choose an image of the invoice... ",type=["jpg", "jpeg", "png"])   ## File Uploader          

## 2.1 Image Display.
if upload_file is not None:       
    image = Image.open(upload_file)
    st.image(image, caption="Upload Image.", use_column_width=True)
else:
    st.error("Please upload an invoice image before proceeding.")

## 2.3 Multiselect Widget
options = st.multiselect(
    "Select information to extract:",
    ["Invoice Number", "Date", "Total Amount / Due", "Vendor Name", "Line Items", "Location / Region"])

## 2.4 Input:
placeholder_text = "Type details here if not in options above..."
input = st.text_input("Ask About Your Invoice: ", key= "input", placeholder= placeholder_text)    
image = ""                                                                                                    ## image variable is initialized to store the image data later


# 3. Language selection
language = st.selectbox("Selct Response Language:", ["English", "Tamil", "Hindi", "German", "Chinese", "French"])


# 4. Submission and Model Interaction.
submit = st.button("Tell me about Invoice")    


# 5. Input Prompt.
## Prompt Text:
input_prompt = """"
As a highly skilled invoice analysis expert, I can extract and interpret information from invoice images with precision. 
Upload an invoice image, and I will answer any questions you have about it, leveraging my deep understanding of invoice structure and content." 
"""

# 5.1 | 2.3 Update input prompt based on selected options
if options:
    input_prompt += " Please focus on extracting the following information: " + ", ".join(options)

# 5.2 | 4 Modify input prompt with language information
input_prompt += f" The invoice is in {language}."



# 6. Error Handling and Output Formatting.
## if submit button is clicked
## Error Handling..Uses try-except blocks to handle potential errors like invalid options, missing files, or other exceptions.
if submit:

    try:
        # Image Processing and Response
        image_data = helper.input_image_details(uploaded_file=upload_file)
        response = helper.get_gemini_response(input=input_prompt, image=image_data, prompt=input)
        extracted_data = helper.extract_information_ner(response)

        # Translate if needed and display
        if language != "English":
            translated_data = helper.language_translate(language, options, extracted_data, input_text=input)
            st.write("**Extracted Information:**")
            if options:
                st.table(translated_data)  # Display translated extracted_data
            else:
                st.write(translated_data)   # Display translated input_text

        else:
            # Display information without translation
            st.write("**Extracted Information:**")
            if options:
                st.table(extracted_data)  # Display only the filtered data
            else:
                st.write(response)

    except KeyError as e:
        st.error(f"Invalid option selected: {e}")  # Handle invalid option)
    except FileNotFoundError as e:
        st.error("No file uploaded or file not found!")
    #except Exception as e:
            #st.error(f"An unexpected error occurred: {e}")


