from flask import Flask
from flask import render_template
from flask import request
from server.get_questions import get_questions
from server.run_prompt import run_prompt
import json

app = Flask(__name__)

transcript = {}

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/", methods=["POST", "GET"])
def joined():
    if request.method == "POST":
        prompt = request.form['txt']
        res = get_questions(prompt)
        transcript["prompt"] = prompt
        return render_template('question.html', text=json.dumps(res), question=res[0])
    return render_template('index.html')

@app.route("/question", methods=['POST', 'GET'])
def next_question():
    if request.method =="POST":
        all_questions = json.loads(request.form["all_questions"])
        all_questions = all_questions[1:]
        transcript[request.form["question"]] = request.form["answer"]
        print(transcript)
        if len(all_questions) == 0:
            res = run_prompt(transcript)
            print(res)
            transcript.clear()
            #mytext = " <br /> ".join(res.split("\n"))
            #print(mytext)
            return render_template('answer.html', response = res)
        else:
            return render_template('question.html', text=json.dumps(all_questions), question=all_questions[0])
        
@app.route("/answer")
def answer_page():
    return render_template('answer.html')


