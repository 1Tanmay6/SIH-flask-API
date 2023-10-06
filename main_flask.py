from llama_cpp import Llama
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
import json
from similarity import cosine_similarity as cs
from guide_ratio import student_guide_matching as gr
from buddymatching import buddymatching as buddy

print('=-=' * 80)
print("Loading flask application...")
print('=-=' * 80)
app = Flask(__name__)
"""
inp = 0

print('=-=' * 80)
print("Loading model...")
print('=-=' * 80)
llm = Llama(model_path="llama-2-7b-chat.ggmlv3.q8_0.bin", n_ctx=256)

print('=-=' * 80)
print("Model loaded.")
print('=-=' * 80)

def answer_giver(str):
    prompt = "Q: " + str + " A: "
    output = llm(prompt,  max_tokens=0)
    return output["choices"][0]['text'].split("A:")[0]

def paper_maker(str):
    cleaned_input = ' '.join(str.split()).replace('\\', '')


    # Extract the title, abstract, and link from the cleaned input string
    title_start = cleaned_input.find('Title: "') + len('Title: "')
    title_end = cleaned_input.find('" Abstract:')
    title = cleaned_input[title_start:title_end]

    abstract_start = cleaned_input.find('Abstract: ') + len('Abstract: ')
    abstract_end = cleaned_input.find(' Link:')
    abstract = cleaned_input[abstract_start:abstract_end]

    link_start = cleaned_input.find('Link: <') + len('Link: <')
    link_end = cleaned_input.find('>', link_start)
    link = cleaned_input[link_start:link_end]

    # Create a dictionary with the extracted information
    paper = {
        "title": title,
        "abstract": abstract,
        "link": link
    }

    print(paper['title'])
    return paper

"""

"""
@app.route('/answer', methods=['GET', 'POST'])
def answer():
    curent_output = ''
    # if request.method == 'GET':
    #! curent_output = answer_giver("give me 1 research paper on the topic of erectile dysfunction give me answer in format Title: 'title', abstract: 'abstract of that paper' and link: 'link of the paper' and make this in form of python dictonary becuase your response is going to be sent to database so dont write anything extra")
    curent_output = answer_giver("give me 1 research paper on the topic of erectile dysfunction give me answer in format Title: 'title', abstract: 'abstract of that paper' and link: 'link of the paper' and make this in form of python dictonary becuase your response is going to be sent to database so dont write anything extra")
    while curent_output == '':
        pass
    print(curent_output)
    json_str = json.dumps(paper_maker(curent_output))
    curent_output = json.loads(json_str)
    print("=-=" * 80)
    print(curent_output)
    return curent_output

"""
@app.route('/similarity', methods=['GET', 'POST'])
def similarity():
    filename = request.args.get('filename')
    file_path = request.args.get('file_path')
    #? http://192.168.7.114:5000/similarity?filename=pcu&file_path=/home/tanmaypatil/Documents/API/similarity/similarity_content
    return {
        'res':cs.percentages(filename, file_path)
    } 

@app.route('/guide_ratio', methods=['GET', 'POST'])
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

@app.route('/buddy_matching', methods=['GET', 'POST'])
def buddy_matching():
    output_list = buddy.output_list_maker()
    return {
        'res':output_list
    }



@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Welcome to the SIH API!'



if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)



#! Later code
# input_str = 'Sure, here is a research paper on the topic of quantum physics in the format you requested: Title: "Exploring the Quantum Realm: A Review of Recent Advances in Quantum Physics" Abstract: "Quantum physics has been a rapidly developing field over the past few decades, with many exciting advancements in our understanding of the behavior of matter and energy at the smallest scales. Here, we review some of the most recent developments in the field, including the observation of quantum gravity, the discovery of new states of matter, and the realization of quantum supremacy. We also discuss the potential applications of these advancements in fields such as cryptography, computing, and materials science." Link: <https://journals.aps.org/prx/pdf/2018/05/100301>'

# # Extract the title, abstract, and link from the input string
# title_start = input_str.find('Title: "') + len('Title: "')
# title_end = input_str.find('" Abstract:')
# title = input_str[title_start:title_end]

# abstract_start = input_str.find('Abstract: "') + len('Abstract: "')
# abstract_end = input_str.find('" Link:')
# abstract = input_str[abstract_start:abstract_end]

# link_start = input_str.find('Link: <') + len('Link: <')
# link_end = input_str.find('>')
# link = input_str[link_start:link_end]

# # Create a dictionary with the extracted information
# paper = {
#     "title": title,
#     "abstract": abstract,
#     "link": link
# }

# print(paper)
