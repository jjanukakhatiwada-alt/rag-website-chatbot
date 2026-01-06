import os
from dotenv import load_dotenv

# This looks for the .env file in your project root
load_dotenv()

# Fetch the variable by the name you used inside the .env file
api_key = os.getenv("OPENAI_API_KEY") 

# Now use 'api_key' in your RAG logic
# Example: client = OpenAI(api_key=api_key)