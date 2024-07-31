#  1.Imports & Setup.
import streamlit as st
import helper

# 2.Streamlit App Initialization
st.set_page_config(page_title="Chat With Multiple PDF")
st.header("Chat With Multiple PDF Using Gemini Demo")

# 3.User Question Input.
user_question=st.text_input("Enter your question about the PDF file:")          ## Creates a text input field in the Streamlit app where the user can type their question about the PDF documents.
if user_question:
    helper.user_input(user_question)


# 4.Sidebar and PDF Upload:
with st.sidebar:
    st.title("Menu.")
    # Creates a sidebar in the Streamlit app and adds a title "Menu." to it

    pdf_doc=st.file_uploader("Upload your pdf file click on submit & Process Button", accept_multiple_files=True)       ## Creates a file uploader widget in the sidebar, allowing users to upload one or multiple PDF files. They are stored in the pdf_doc variable.
    if st.button("submit & Process"):
        with st.spinner("Processing...."):              ##A spinner with the text "Processing...." is displayed, indicating that the app is working.
            raw_text = helper.read_pdf_text(pdf_doc)                ## Read all the PDF Text. helper module is called with the uploaded pdf_doc as an argument. This function extracts all text from the PDFs and returns it as raw_text
            text_chunks = helper.get_text_chunks(raw_text)          ## Text Splitting. helper module is called with the raw_text as an argument. This function splits the text into smaller chunks for easier processing.
            helper.get_chunks_into_vectorstore(text_chunks)         ## Embedding all Text Chunks. function is called with the list of text chunks. This function converts the chunks into vector representations and stores them in a vector database.
            st.success("Done")


## success message "Done" is displayed, indicating that the processing is complete and the app is ready to answer questions about the uploaded PDFs.