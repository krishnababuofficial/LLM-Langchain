# 1. Importing Libraries:
import streamlit as st
import helper


# 2. Setting Page Configuration:
st.set_page_config(page_title="Generate Blogs",                         ## st.set_page_config: This configures the Streamlit app's appearance:  | page_title: Sets the title displayed in the browser tab.    
                   page_icon= "🖥️ 🖨️ 📄",                              ## Sets the emoji icon displayed in the browser tab.
                   layout="centered",                                   ## Sets the layout of the app to "centered".
                   initial_sidebar_state="collapsed")                   ## Sets the initial state of the sidebar to "collapsed".



# 3. Header and Input Field:
st.header("Generate Blog 🖥️ 🖨️ 📄")                         ## Creates a header on the page with the specified text and emoji.
input_text = st.text_input("Enter the Blog Topic")           ## Creates a text input field where users can enter the desired blog topic


# 4. Additional Input Fields:
col1, col2 = st.columns([5,5])              ## Creates two columns with equal width (5 units each) for better layout.

with col1:      ## Places the following element in the first column
    no_words = st.text_input("Word Limit: (e.g. 100 or 300)")
with col2:     ## Places the following element in the second column
    blog_style = st.selectbox("Writing the blog for",
                              ("Researchers","Data Scientist","common people"), index = 0)
    
    
# 5. Submit Button and Response:    
submit = st.button("Generate")              ## Creates a button labeled "Generate".

## Final response 
if submit:
    st.write(helper.get_llama_reponse(input_text,no_words,blog_style))      ## Calls the get_llama_reponse function from the helpers module with the user-provided input text, word count, and blog style.
## st.write: Displays the generated blog post on the Streamlit app.
