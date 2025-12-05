from VectorDB import model
from llm import aimodel
from system_prompt import systemPrompt

def retreival(st , prompt):
    # we need to search this prompt on the vector DB 
    
    similarityContext = model.similarity_search(prompt)
    print(prompt , similarityContext)
    sysPrompt = systemPrompt(similarityContext)
    
    st.session_state.messages.insert(0,{"role":"system","content":sysPrompt})
    # {"role":"user","content":promp} # isko ak alag array mein daltun main
    # print("======================================")
    # print(st.session_state.messages)
    # print("======================================")
    
    llmout = aimodel.invokeLLm(str(st.session_state.messages))
    # print(llmout)
    return {"role":"agent","content":llmout.content}