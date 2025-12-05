from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
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


    # we need to initialize faiss db or something 

    model = "sentence-transformers/all-mpnet-base-v2"
    embedder = HuggingFaceEndpointEmbeddings(
        model=model,
        task="feature-extraction",
    )
    qdrant_client = os.getenv("QDRANT_CLIENT")
    client = QdrantClient(qdrant_client)
    
    if client.collection_exists(collection_name="rag-2") != True:
        client.create_collection(
            collection_name="rag-2",
            vectors_config=VectorParams(size=768,distance=Distance.COSINE)
        )
        
    vectorStore = QdrantVectorStore(
        client=client,
        collection_name="rag-2",
        embedding=embedder
    )
    vectorStore.add_documents(splitted)