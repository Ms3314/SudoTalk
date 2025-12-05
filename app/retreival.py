from VectorDB import model
def retreival(prompt):
    # we need to search this prompt on the vector DB 
    output = model.similarity_search(prompt)
    llmout = ""
    return {"role":"","content":llmout}