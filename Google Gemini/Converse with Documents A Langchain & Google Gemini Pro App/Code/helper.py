# 1. Imports and Setup.
import os                                                   ## os and dotenv: For managing environment variables and API keys.
from dotenv import load_dotenv
                                                         
import streamlit as st
from PyPDF2 import PdfReader                                                        ## To read and extract text from PDF documents.
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain_core.prompts.prompt import PromptTemplate

# Configuration.
load_dotenv()                                               ##  Loads environment variables from a .env file.
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))        ## Sets the API key for Google Generative AI.

# 2. Processing PDF Documents:

# Read the PDF that as been uploaded. Extract all text from the uploaded PDF. 
def read_pdf_text(uploaded_pdf_doc):        
    text = ""                                       ## Create Text Variable
    for pdf in uploaded_pdf_doc:                    ## Read All The Pages In Upload_doc
        pdf_reader = PdfReader(pdf)                 ## Read this with the help of PdfReader,This Reader Wil Read all the Pages and Basically it's in form of List
        for pages in pdf_reader.pages:              ## For page in the pdf_reader going to read all the pages in it so we will be usig ".pages"
            text+=pages.extract_text()              ## From this Particular Page We are going to Extract all the Text
    return text                                     ## return the extracted text                

# Divide thise text in to smaller & manageable chunks.
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size= 10000, chunk_overlap= 1000)
    chunks = text_splitter.split_text(text)         ## Splitting Text into Chunks Based on the text_splitter Assigned
    return chunks


## read_pdf_text(uploaded_pdf_doc):
        ## This function takes a list of uploaded PDF files.
        ## It loops through each PDF, extracts the text from all pages, and concatenates it into a single string.
        ## The extracted text is then returned.

## get_text_chunks(text):
        ## This function takes the extracted text as input.
        ## It uses RecursiveCharacterTextSplitter from Langchain to split the text into smaller chunks with a specified size and overlap.
        ## The list of chunks is returned.


# 3.Creating Vector Store
def get_chunks_into_vectorstore(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding= embeddings)            ## All Text Chunks and Embedding with the Mentioned Embeddings 
    vector_store.save_local("faiss_index")                                          ## Innside "faiss_index" will be able to see the vectors this will be stored(saved) in local

## This function takes the list of text chunks.
        ## It uses GoogleGenerativeAIEmbeddings to convert each chunk into a vector representation.
        ## It creates a FAISS vector store and adds the chunks with their corresponding vectors.
        ## The vector store is saved locally as "faiss_index".


#4. Building Conversational Chain.

## This function sets up the question-answering chain.
        ## It initializes ChatGoogleGenerativeAI with the "gemini-pro" model and sets the temperature.
        ## It defines a prompt template that provides context and asks a question.
        ## It uses load_qa_chain to create a chain of type "stuff" with the specified model and prompt.
        ## The chain is returned.

def get_conversational_chain():      
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)  
    
    prompt_temp = """
    You are a helpful and accurate AI assistant. Your task is to answer the question based on the provided context ONLY. 
    Do not make assumptions or fabricate information that is not explicitly stated in the context. If the answer cannot be found in the context, simply state: "Answer not available in the context\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    #prompt_templates = {
    #"template": prompt_temp
    #}

    prompt = PromptTemplate(template = prompt_temp, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type= "stuff",prompt= prompt)                              ## "stuff"- also need to do internal text summerization
    return chain



#5. Handling User Input
def user_input(user_question):                                                                      ## takes the user's question as a string input..

    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")                       ## This is needed to embed the user's question for comparison with the document chunks.
    ## Creates a GoogleGenerativeAIEmbeddings object using the same embedding model as before ("models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)      ## Loads the previously saved FAISS vector store from the "faiss_index" file.
    ## The allow_dangerous_deserialization=True option is used here, which might have security implications and should be carefully considered
    
    docs = new_db.similarity_search(user_question)                                                  ## Performs a similarity search on the vector store using the user's question as input. 
    ## This will retrieve the most relevant document chunks based on their vector similarity to the user's question. The results are stored in the docs variable.
    
    chain = get_conversational_chain()      ## Retrieves the conversational chain created earlier 
    

    response  = chain(                                                      ## Runs the chain with a dictionary containing two keys
        {"input_documents":docs,                                            ## This provides the list of relevant document chunks (docs) retrieved from the similarity search
         "question":user_question},                                         ## This provides the user's question as input to the chain.
        return_only_outputs=True                                            ##  used to only return the final output of the chain
        )
    
    print(response)
    st.write("Reply: ", response["output_text"])

    ## Extracts the "output_text" field from the response dictionary and displays it in the Streamlit app with the label "Reply: ".
    ## This is the final answer generated by the chain based on the user's question and the relevant context from the documents


