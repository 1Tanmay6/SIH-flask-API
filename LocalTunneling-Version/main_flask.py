from llama_cpp import Llama
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import json
from similarity import cosine_similarity as cs
from guide_ratio import student_guide_matching as gr
from buddymatching import buddymatching as buddy
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler  
from flask_lt import run_with_lt


print('=-=' * 20)
print("Loading flask application...")

app = Flask(__name__)
print('=-=' * 20)
print("Creating a Tunneled Link...")

run_with_lt(app)

@app.route('/answer', methods=['GET', 'POST'])
def answer():
    # query params extraction
    prompt = request.args.get('prompt')
    llm = Ollama(model="mistral", 
                callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))
    answer = llm(prompt, max_tokens=5, stop="###")

    # Convert the string response to a Python dictionary
    data = json.loads(answer)

    # Return the dictionary as a JSON response
    return jsonify(data)

#! Give me 2 research paper on breast cancer give everything in a list of {} include title,author,year,abstract of at max 30 words, link and all the list should be in a object {res: } make it parsable by json.loads dont write anything else in the response or add qoutes or anything else


@app.route('/getSimilarities', methods=['GET', 'POST'])
def similarity():
    filename = request.args.get('filename')
    file_path = request.args.get('file_path')
    #? http://192.168.7.114:5000/similarity?filename=pcu&file_path=/home/tanmaypatil/Documents/API/similarity/similarity_content
    return {
        'res':cs.percentages(filename, file_path)
    } 

@app.route('/getGuideRatio', methods=['GET', 'POST'])
def guide_ratio():
    class Person:
        def __init__(self, name, pref, count=None):
            self.name = name
            self.pref = pref
            self.count = count if count is not None else len(pref)

        def to_dict(self):
            return {'name': self.name, 'pref': self.pref, 'count': self.count}


    db_st = [{
        'name': 'Megha',
        'pref': ['ai_ml','ds','iot'],
    },

    {
        'name': 'Shounak',
        'pref': ['chemical','testtubes','bioinformatics'],
    },
    {
        'name': 'Nayra',
        'pref': ['ai_ml','ds','iot'],
    },
    {
        'name': 'Navya',
        'pref': ['chemical','testtubes','bioinformatics'],
    },
    {
        'name': 'Navya1',
        'pref': ['ai_ml','ds','iot'],
    },
    {
            'name': 'Navya2',
            'pref': ['ai_ml','ds','iot'],
    }]



    db_te = [  {
            'name': 'james',
            'pref': ['chemical','testtubes','bioinformatics'],
            'count': 5  # Assuming a teacher can take 2 students
        },

        {
            'name': 'james1',
            'pref': ['ai_ml','ds','iot'],
            'count': 1  # Assuming a teacher can take 1 student
        },
        {
            'name' : 'Joseph',
            'pref': ['ai_ml','ds','iot'],
            'count': 1
        } ]

    te = [Person(te['name'], te['pref'], te['count']) for te in db_te]
    st = [Person(st['name'], st['pref']) for st in db_st]

    teachers = [teacher.to_dict() for teacher in te]
    students = [student.to_dict() for student in st]


    return {
        'res':gr.match_students_teachers(students=students, teachers=teachers)
    }

@app.route('/getBuddies', methods=['GET', 'POST'])
def buddy_matching():
    output_list = buddy.output_list_maker()
    return {
        'res':output_list
    }



@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Welcome to the SIH API!'



if __name__ == '__main__':
    # print('=-=' * 20)

    # print('Use this: ' + url)
    # print('=-=' * 20)
    app.run()
