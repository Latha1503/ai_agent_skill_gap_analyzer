import os
from groq import Groq
from dotenv import load_dotenv

# Load API key
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

# Connect to Groq
client = Groq(api_key=api_key)

# Send a question to AI
response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "A customer paid 2000 rupees but their order was not placed. Analyze this complaint."
        }
    ]
)

# Display AI response
print(response.choices[0].message.content)