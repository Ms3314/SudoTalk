from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from VectorDB import model
import os
import tempfile

def indexing(fileupload):
    # Create temporary file for PDF processing
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    temp.write(fileupload.read())
    temp.close()  # Close the file so it can be read by PyPDFLoader
    
    try:
        # Load and process the PDF
        loader = PyPDFLoader(temp.name)
        docs = loader.load()
        print(f"📄 Loaded {len(docs)} pages from PDF")
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
        splitted = text_splitter.split_documents(docs)
        print(f"📋 Split into {len(splitted)} chunks")
        
        # Print first chunk for debugging
        if splitted:
            print(f"🔍 Sample chunk: {splitted[0].page_content[:200]}...")
        
        # Create DB and add documents
        model.creatDB("rag-24")
        model.add_documents(splitted)
        print(f"✅ Added {len(splitted)} documents to vector DB")
        
    finally:
        # Clean up temporary file
        os.unlink(temp.name) 