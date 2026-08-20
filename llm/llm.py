import os
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.llms.groq import Groq

def configure_llm():
    # Load environment variables from .env file
    load_dotenv()
    
    # Get the Groq API key from environment
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")
        
    # Initialize Groq LLM (llama3-8b-8192 is a fast default model)
    llm = Groq(model="openai/gpt-oss-120b", api_key=api_key)
    
    # Set it as the global LlamaIndex LLM
    Settings.llm = llm
    
    print("[SUCCESS] Groq LLM Configured")
