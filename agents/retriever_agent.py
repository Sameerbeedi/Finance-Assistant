# agents/retriever_agent.py
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def create_vector_store(documents):
    embedding = OpenAIEmbeddings()
    vectordb = FAISS.from_texts(documents, embedding)
    return vectordb
