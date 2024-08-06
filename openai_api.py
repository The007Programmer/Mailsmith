from openai import OpenAI
import json

# Open json file with openai api key.
with open("secrets/openai_key.json", "r") as keyfile:
    data = json.load(keyfile)

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=data["OPENAI_API_KEY"])

# Make the API call
completion = client.Completion.create(
    model="gpt-4o-mini",
    prompt="Compose a poem that explains the concept of recursion in programming.",
    max_tokens=150
)

# Print the response
print(completion.choices[0].text.strip())