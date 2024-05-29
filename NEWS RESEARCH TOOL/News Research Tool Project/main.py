import os
import streamlit as st
import time
from langchain_openai import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import SeleniumURLLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()   # takes environment variables from .env

st.title("News Research Tool")
st.sidebar.title("News Article URLs")

# 3 Urls one below other
urls = [] # Urls stored
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

processed_url_click = st.sidebar.button("Process URLs")

main_placefolder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)

vectorstore_openai = None

if processed_url_click:
    # Load data
    loader = SeleniumURLLoader(urls = urls)
    main_placefolder.text("Data Loading. .....STARTED.... . .")
    data = loader.load()
    # Split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators = ["\n\n", "\n", ".", ","],
        chunk_size = 1000
    )
    main_placefolder.text("Text Splitter. .....STARTED.... . .")
    docs = text_splitter.split_documents(data)
    # Create embeddings and save it to faiss
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placefolder.text("Embedding Vector Started Building. . .")
    time.sleep(2)


query = main_placefolder.text_input("Question: ")

if query:
    if vectorstore_openai:  # Check if vectorstore_openai is defined
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore_openai.as_retriever())
        results = chain({"question": query}, return_only_outputs=True)
        # results op {"answer": "","source" : [] } result will be dict.
        st.header("Answer")
        st.write(results["answer"])

    # Display Source, if available
        sources= results.get("sources", "")
        if sources:
            st.subheader("Sources:")
            source_list = sources.split("\n") # split the sources by new line
            for source in source_list:
                st.write(source)

    else:
        st.error("Please process URLs first.")