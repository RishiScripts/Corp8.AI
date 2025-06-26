from dotenv import load_dotenv
import os

# Step 1: Load environment variables from the .env file
load_dotenv()

# Step 2: Retrieve your API keys
openai_key = os.getenv("OPENAI_API_KEY")
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Step 3: Use them in LangChain or verify they're loaded
print("OpenAI Key Loaded:", bool(openai_key))
print("Hugging Face Token Loaded:", bool(hf_token))
