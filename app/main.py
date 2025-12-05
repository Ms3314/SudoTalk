# we need to make a Streamlit based RAG pdf/web LLM agent 
import streamlit as st
from indexing import indexing
from retreival import retreival
from dotenv import load_dotenv
import os 

load_dotenv()

st.header("SudoTalk : Your RAG based LLM agent")

fileupload = st.file_uploader("upload pdf" , accept_multiple_files=False , type=["pdf"])

if fileupload is not None:
    # we give the pdf for the indexing phase 
    indexing(fileupload)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message("user"):
    st.write("Hello !")

    
if prompt := st.chat_input("Talk to pdf"):
    with st.char_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user","content":prompt})
    
    llmout = retreival(prompt)
    st.session_state.messages.append(llmout)
    
    
    

    
    
    
    

    
