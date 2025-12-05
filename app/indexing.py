from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from VectorDB import model
import os
import tempfile

def indexing(fileupload):
    temp = tempfile.NamedTemporaryFile(delete=False,suffix=".pdf")
    temp.write(fileupload.read())
    loader = PyPDFLoader(temp.name)
    docs = loader.load()
    # print(docs["page_content"])
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000 , chunk_overlap=300)
    splitted = text_splitter.split_documents(docs)

    model.creatDB("rag-24")
    model.add_documents(splitted)
    # we want to add documents 