from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from qdrant_client.http.models import Distance, VectorParams


from dotenv import load_dotenv 
import os
load_dotenv()
qdrant_client = os.getenv("QDRANT_CLIENT")

# what I want to do it make a constructor and then be able to import this embedding model at different places 


"""
    we are using camel case for the private methoods 
    we will be using _ case for the public methoods
"""


class VectorDB:
    def __createClient(self):
        self._client = QdrantClient(qdrant_client)
    
    # this is an absraction over the whole emedding layer 
    def __createVectorStore(self):
        self._vectorStore = QdrantVectorStore(
            client=self._client,
            collection_name=self._collection_name,
            embedding=self._embedder
        )
        
    def __CreateEmbeddingModel(self):
        model = "sentence-transformers/all-mpnet-base-v2"
        self._embedder = HuggingFaceEndpointEmbeddings(
            model=model,
            task="feature-extraction",
        )

    # jab initialize karte jab khali client iniialize hota
    def __init__(self ):
        self.__createClient()
        
    
    def creatDB(self , collection_name):
        self.__CreateEmbeddingModel(self)
        self.__createCollection(self ,collection_name)
        self.__createVectorStore(self)
    
    def __createCollection(self , collection_name):
        self._collection_name = collection_name
        if self._client.collection_exists(collection_name) != True:
            self._client.create_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(size=768,distance=Distance.COSINE)
            )
    def add_documents(self , documents):
        self._vectorStore.add_documents(documents)
        
    def similarity_search(self , query):
        return self._vectorStore.similarity_search(query)

model = VectorDB()