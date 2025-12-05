import os
from dotenv import load_dotenv
load_dotenv()

class llm:
    def __llmInitialize(self):
        # self.llm = 
        pass

    def invokeLLm(self , query):
        self.llm.invoke(query)
        
    def __init__(self):
        self.__llmInitialize()
        pass