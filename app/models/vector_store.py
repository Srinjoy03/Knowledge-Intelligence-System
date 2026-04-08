import chromadb
from langchain_community.vectorstores import Chroma 
# UPGRADED: Using free, local HuggingFace embeddings instead of Google API
from langchain_community.embeddings import HuggingFaceEmbeddings

# --- HISTORICAL REFERENCE ---
# Originally tried using GoogleGenerativeAIEmbeddings (models/gemini-embedding-001)
# Removed on 8th April due to Google API instability (500 Internal / 404 Not Found errors)
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# self.embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
# ----------------------------


class VectorStore:
    def __init__(self, path):
        # This model runs entirely on your machine. No API key needed!
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        
        self.vector_store = Chroma(
            persist_directory=path, 
            embedding_function=self.embeddings
        )
    
    def add_documents(self, documents):
        self.vector_store.add_documents(documents)
    
    def similarity_search(self, query, k=4):
        return self.vector_store.similarity_search(query, k=k)