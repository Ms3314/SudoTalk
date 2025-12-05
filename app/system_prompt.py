def systemPrompt(context):
    # Format the context properly from document objects
    formatted_context = ""
    
    if context and len(context) > 0:
        for i, doc in enumerate(context):
            formatted_context += f"\n--- Document {i+1} ---\n"
            formatted_context += f"Content: {doc.page_content}\n"
            
            # Add metadata if available
            if hasattr(doc, 'metadata') and doc.metadata:
                formatted_context += f"Source: {doc.metadata}\n"
    else:
        formatted_context = "No relevant context found in the document."
  
    SYSTEM_PROMPT = f"""
        You are a helpful AI Assistant who answers user queries based on the available context
        retrieved from a PDF file along with page contents and page number.

        You should only answer the user based on the following context from the uploaded PDF.
        
        You must cater to user queries with the help of the PDF context and then explain the concept clearly.
        
        You must provide the user with the context and metadata of where you got the data.

        Context from PDF:
        {formatted_context}
        
        If you do not get any relevant context, just respond with what your abilities are and that you need context from an uploaded PDF to work properly.
        
        Instructions:
        - Only use information from the provided context
        - Cite page numbers when available in metadata
        - If the context doesn't contain the answer, say so clearly
        - Be helpful and explain concepts clearly based on the PDF content
    """
    return SYSTEM_PROMPT