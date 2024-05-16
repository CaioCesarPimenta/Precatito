import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import os

haders = {
    "autorisation": st.secrets["OPENAI_API_KEY"],
    "content-type": "application/json"
}

def PDF():

    OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    
    def extract_text_from_pdf(pdf_file):
        pdf_reader = PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    # Function to process multiple PDF files
    @st.cache_data
    def process_pdfs(pdf_files):
        all_texts = ""
        for pdf_file in pdf_files:
            text = extract_text_from_pdf(pdf_file)
            all_texts += text + "\n"
        return all_texts

    # Upload multiple files
    uploaded_files = st.file_uploader("Me mostre o seu processo em formato .PDF(Evite muitas imagens)", type="pdf", accept_multiple_files=True)
    
    if uploaded_files:
        all_texts = process_pdfs(uploaded_files)
        
        # Split into chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(all_texts)
        
        # Create embeddings
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY, model="text-embedding-ada-002")
        knowledge_base = FAISS.from_texts(chunks, embeddings)
        
        # Show user input
        user_question = st.text_input("Pergunte ao Precatito Goul:")
        if user_question:
            docs = knowledge_base.similarity_search(user_question)
            llm = OpenAI(openai_api_key=OPENAI_API_KEY)
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=user_question)
                print(cb)
                
            st.write(response)
