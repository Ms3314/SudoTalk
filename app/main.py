# we need to make a Streamlit based RAG pdf/web LLM agent 
import streamlit as st
from indexing import indexing
from retreival import retreival
from dotenv import load_dotenv
from system_prompt import systemPrompt
import os 

load_dotenv()

# Page configuration
st.set_page_config(
    page_title="SudoTalk - RAG Assistant", 
    page_icon="🤖"
)

# Main header
st.title("🤖 SudoTalk")
st.subheader("Your RAG based LLM agent")

# Sidebar
with st.sidebar:
    st.header("📋 Instructions")
    st.write("""
    1. Upload your PDF document
    2. Wait for processing to complete
    3. Ask questions about your document
    4. Get intelligent responses
    """)
    
    st.header("ℹ️ About")
    st.write("SudoTalk uses advanced AI to understand your documents and provide accurate answers.")

# File upload section
st.header("📄 Upload Your PDF Document")

# Check if PDF is already uploaded
if "pdf_processed" in st.session_state and st.session_state.pdf_processed:
    st.success("✅ PDF Ready for Questions")
else:
    st.info("⏳ Upload PDF to Begin")

fileupload = st.file_uploader(
    "Choose a PDF file", 
    accept_multiple_files=False, 
    type=["pdf"]
)

if fileupload is not None:
    with st.spinner("Processing your PDF..."):
        indexing(fileupload)
        st.session_state.pdf_processed = True
    st.success("PDF processed successfully!")

# Chat section
st.header("💬 Chat with Your Document")

# Initialize chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({"role":"system","content":systemPrompt})

# Display chat messages
for messages in st.session_state.messages:
    if messages["role"] != "system":
        role = "assistant" if messages["role"] == "agent" else messages["role"]
        with st.chat_message(role):
            st.markdown(messages["content"])

# Chat input
if prompt := st.chat_input("Ask a question about your PDF document..."):
    if "pdf_processed" not in st.session_state or not st.session_state.pdf_processed:
        st.error("Please upload and process a PDF document first.")
        st.stop()
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role":"user","content":prompt})
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            llmout = retreival(st , prompt)
        st.markdown(llmout["content"])
    
    st.session_state.messages.append(llmout)

# Sidebar settings
with st.sidebar:
    st.divider()
    st.header("🔧 Settings")
    
    if st.button("Clear Chat History"):
        if "messages" in st.session_state:
            st.session_state.messages = [msg for msg in st.session_state.messages if msg["role"] == "system"]
        st.rerun()
    
    if st.button("Reset Session"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
    
    # Session stats
    if "messages" in st.session_state:
        user_messages = len([msg for msg in st.session_state.messages if msg["role"] == "user"])
        if user_messages > 0:
            st.divider()
            st.header("📊 Session Stats")
            st.metric("Questions Asked", user_messages)
    
    
    
    

    
    
    
    

    
