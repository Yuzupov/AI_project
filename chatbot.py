import openai
import os
from openai import OpenAI

with open('apikey.txt', 'r') as file:
    OPENAI_API_KEY = file.read().strip() 

client = OpenAI(api_key=OPENAI_API_KEY)

modelId = "ft:gpt-3.5-turbo-0125:scrumai::AgYTUrrD"

def takeInAndOutputRespone(userPrompt):
    completion = client.chat.completions.create(
        model=modelId,
        messages=[
            {"role": "assistant", "content": "You are an expert scrum master."},
            {
                "role": "user",
                "content": userPrompt
            }
        ]
    )
    print(completion.choices[0].message.content)


def main():
    while(True):
        prompt = input("Enter your scrum related prompt here: ")
        takeInAndOutputRespone(prompt)

main()
