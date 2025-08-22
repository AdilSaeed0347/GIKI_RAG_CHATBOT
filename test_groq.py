import os
from groq import Groq
import httpx
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
print("API Key (partial):", api_key[:10] + "..." if api_key else "Not found")
try:
    client = Groq(api_key=api_key, http_client=httpx.Client(proxies=None))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Test query"}],
        max_tokens=10
    )
    print("Test Response:", response.choices[0].message.content)
except Exception as e:
    print("Error:", str(e))