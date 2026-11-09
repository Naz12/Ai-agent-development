import os
import litellm
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HIVE_API_KEY")

messages = [
    {"role": "system", "content": "You are an expert software engineer."},
    {"role": "user", "content": "Write a function to swap dictionary keys and values."}
]

response = litellm.completion(
    model="openai/deepseek-ai/deepseek-v4.1-flash-1017",
    messages=messages,
    api_key=api_key,
    api_base="https://api.thehive.ai/api/v3",
    custom_llm_provider="openai"
)

print(response.choices[0].message.content)