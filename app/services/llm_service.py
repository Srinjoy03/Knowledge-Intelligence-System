from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.memory import ConversationBufferMemory
from config import config

class LLMService():
    def __init__(self, vector_store):
        # Point to the currently active free-tier model
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", 
            temperature=0.7,
            google_api_key=config.GOOGLE_API_KEY
        )

        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.vector_store.as_retriever(),
            memory=self.memory 
        )
    
    def get_response(self, query):
        try:
            response = self.chain.invoke({"question": query}) 
            return response["answer"]
        except Exception as e:
            print(f"Error in getting LLM response: {e}")
            return "I encountered an error while processing your request"