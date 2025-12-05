# we need to make a Streamlit based RAG pdf/web LLM agent 
import streamlit as st
from app.indexing import indexing
from dotenv import load_dotenv
import os 

load_dotenv()

st.write("SudoTalk : Talk to your PDF !! ")

fileupload = st.file_uploader("SudoTalk" , accept_multiple_files=False , type=["pdf"])

if fileupload is not None:
    # we give the pdf for the indexing phase 
    indexing(fileupload)
    
    
    
    
    

    
    
    
    

    
