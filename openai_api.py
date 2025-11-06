from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a short bedtime story about a unicorn."
)

print(response.output_text)