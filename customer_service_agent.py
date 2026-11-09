import os
from google.colab import userdata
api_key = userdata.get('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = api_key
from litellm import completion
from typing import List, Dict


def generate_response(messages: List[Dict]) -> str:
    """Call LLM to get response"""
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024
    )
    return response.choices[0].message.content


what_to_help_with = input("What do you need help with?")

messages = [
    {"role": "system", "content": "You are a helpful customer service representative. No matter what the user asks, the solution is to tell them to turn their computer or modem off and then back on."},
    {"role": "user", "content": what_to_help_with}
]

response = generate_response(messages)
print(response)