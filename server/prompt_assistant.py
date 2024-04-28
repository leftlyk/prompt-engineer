import os
from openai import OpenAI
from api import dict

client = OpenAI(
    api_key=dict["OpenAI"]
)

res = input("Prompt: ")


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a prompt engineer and your job is to ask a series of questions to greatly improve the efficacy of prompts."},
    {"role": "user", "content": "Use the prompt, found inside '<>', to devise a series of questions to improve its effectiveness for LLMs: <" + res + "> IMPORTANT: format six questions with no numbers and lines separating them."}
  ]
)



qs = (completion.choices[0].message.content).split('?')

questions_dict = {}

for q in qs: 
    answer = input(q + "? ")
    questions_dict[q] = answer

transcript = "Prompt: " + res + "/n"
for question in questions_dict.keys():
    transcript += question + "? " + questions_dict[question]

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are to construct a detailed and high-quality response to the following transcript based on information you are given."},
    {"role": "user", "content": "Use the entire supplied transcript, including the original prompt and following questions to construct a piece of text, using the transcript as a detailed blueprint. The transcript is found inside '<>'. <" + transcript + "> "}
  ]
)
    
print(completion.choices[0].message.content)