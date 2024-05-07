import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

client = OpenAI(
    api_key=os.getenv("API_KEY")
)

def get_questions(prompt):
    res = prompt


    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a prompt engineer and your job is to ask a series of questions to greatly improve the efficacy of prompts."},
        {"role": "user", "content": "Use the prompt, found inside '<>', to devise a series of questions to improve its effectiveness for LLMs: <" + res + "> IMPORTANT: format six questions with no numbers and lines separating them."}
    ]
    )


    #print(completion.choices[0].message.content)

    qs = (completion.choices[0].message.content).split('?')
    return qs[:-1]