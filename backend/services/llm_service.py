from langchain_groq import ChatGroq
from utils.config import GROQ_API_KEY

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=GROQ_API_KEY
)

def generate_response(prompt: str):
    response = llm.invoke(prompt)
    return response.content