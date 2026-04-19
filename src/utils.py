from crewai import LLM 
import os
from dotenv import load_dotenv 
load_dotenv()


llm = LLM(
    api_key = os.getenv('GROQ_API_KEY'), 
    model="groq/llama-3.1-8b-instant"
)

