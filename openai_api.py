from openai import OpenAI
import json

# Open json file with openai api key.
with open("secrets/openai_key.json", "r") as keyfile:
    data = json.load(keyfile)

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=data["OPENAI_API_KEY"])

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)