import os
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

hugginface_api = os.getenv("HUGGINGFACEHUB_API_TOKEN")



class llm:
    def __llmInitialize(self):
        # self.llm = 
            self.llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
                # other params...
            )

        

    def invokeLLm(self , query):
        # print("-------------------------------")
        # print("invoking an llm")
        # print(query)
        return self.llm.invoke(query)
        
    def __init__(self):
        self.__llmInitialize()
        

aimodel = llm()
