import os
from openai import OpenAI
from server.api import dict

client = OpenAI(
    api_key=dict["OpenAI"]
)

def run_prompt(dictionary):
    transcript = ""
    for question in dictionary.keys():
        transcript += question + "? " + dictionary[question]

    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are to construct a detailed and high-quality answer based on a provided transcript."},
        {"role": "user", "content": "You have been given the following prompt: <Prompt: " + dictionary["prompt"] + "> Use the transcript provided as a set of specifications for what you are to produce. The transcript is found inside '<>'. <" + transcript + "> "}
    ]
    )
        
    return completion.choices[0].message.content