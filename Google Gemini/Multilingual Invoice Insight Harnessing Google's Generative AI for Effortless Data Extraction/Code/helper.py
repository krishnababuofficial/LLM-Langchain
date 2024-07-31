# 1. Imports and Setup.
import os
from dotenv import load_dotenv
load_dotenv()                               ##  os is for interacting with the operating system, and dotenv is used to load environment variables from a .env file.

import google.generativeai as GenAi
GenAi.configure(api_key = os.getenv("GOOGLE_API_KEY"))
## load_dotenv() loads environment variables from the .env file. This is likely where the GOOGLE_API_KEY is stored for accessing the Generative AI API.

import spacy
nlp = spacy.load("en_core_web_sm")          ## for named entity recognition (NER)

from googletrans import Translator
translator = Translator()                   ## Initializes the Translator object from googletrans for language translation.
import pandas


# 2. Loading Gemini Pro Vision Model.
model = GenAi.GenerativeModel('gemini-pro-vision')
## A GenerativeModel object named model is created using the gemini-pro-vision model ID. This indicates that the script intends to use the Gemini Pro Vision model for its tasks.


# 3. get_gemini_response Function.
def get_gemini_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])     ##In Gemini Pro they take all Parameter in the List
    return response.text
## Takes 3 Argument.
## Input: Input is basically what i want the assistant to do w.r.t to the image given(Behaviour of Model), [This likely specifies the desired behavior or task for the model]
## Image: Basically image need to want, [This should be a list containing image data (presumably obtained from input_image_details)]
## Prompt: Is bassically what message i want, [This is a text prompt providing additional context or instructions for the model.]

## The function calls model.generate_content with a list containing the input, image data, and prompt. This sends the data to the Gemini Pro Vision model for processing.
## The model's response is then accessed using .text to extract the text content, which is returned by the function.


# 4. input_image_details Function:
def input_image_details(uploaded_file):                                 ## This function takes an uploaded_file as input, which is assumed to be an uploaded image file.
    if uploaded_file is not None:                                       ## File Check: It checks if the file is not None (meaning a file was actually uploaded).
        #Read file into bytes
        bytes_data = uploaded_file.getvalue()                           ## Data Extraction: If a file exists, it reads the file content into bytes_data and creates a list called image_parts.

        image_parts = [
            {
                "mime_type": uploaded_file.type,     # Get the mime type of the uploaded file, [The mime_type of the uploaded file is extracted and included along with the image data in a dictionary within the image_parts list.]
                "data": bytes_data
                ## MIME: Multipurpose Internet Mail Extensions.  
                #It's a standard way of indicating the type of content being transmitted. In the context of web applications and file uploads 
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    

# 5. Named Entity Recognition on the model's response
def extract_information_ner(text):                                                          #  extracted text (text) as input
    doc = nlp(text)
    extracted_data = {}
    for ent in doc.ents:                                                                    # Iterates through the identified entities and checks if their labels belong to a specific set
        if ent.label_ in [
            "ORG", "DATE", "MONEY", "CARDINAL", "GPE", "PERSON", 
            "PRODUCT", "LAW", "LANGUAGE", "QUANTITY", "NORP", "FAC" 
            ]:  # Adjust entity types as needed
            extracted_data[ent.label_] = ent.text

    return extracted_data                                                                   # Returns the extracted_data dictionary.


# 6. googletrans library
def language_translate(language, options, extracted_data, input_text):
    if language!="English":
        if options:                                                                         # Translate extracted_data if options are selected
            for key, value in extracted_data.items():
                extracted_data[key] = translator.translate(value, dest=language).text
            return extracted_data                                                           # Return translated extracted_data
               
        elif isinstance(input_text, dict):  # Check if input_text is a dictionary
            for key, value in input_text.items():
                input_text[key] = translator.translate(value, dest= language).text
            return input_text
        
        elif isinstance(input_text, str):  # Check if input_text is a string
            input_text =  translator.translate(input_text, dest= language).text
            return input_text  
        


##language_translate Function:
##Takes the desired language, selected options, extracted data, and input text as arguments.
##Checks if the language is not English:
##If options are provided, translates the values in the extracted_data dictionary to the specified language and returns the translated dictionary.
##Alternatively, if input_text is provided, it checks if it's a dictionary or a string and translates its values or the entire string to the specified language and returns the translated result.
##If the language is English or no options/input text are provided, returns the original extracted_data without translation.        