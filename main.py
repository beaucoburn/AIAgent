import os
from dotenv import load_dotenv
from google import genai

client = genai.Client(api_key=api_key)

response = client.models.generate_content()

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

def main():
    print("Hello from aiagent!")


if __name__ == "__main__":
    main()
