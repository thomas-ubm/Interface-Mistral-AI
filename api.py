
"""
@app.get('/')
def root():
    return "Hello World !"

@app.get('/square')
def square(n:int):
    return n*n

"""


"""
from transformers import pipeline

messages = [
    {"role": "user", "content": "Who are you?"},
]
pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")
pipe(messages)

"""

from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
#pipe = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.3")


@app.get("/mistralai")
def index(prompt:str="Who are you?"):
    messages = [
        {"role": "user", "content":prompt},
    ]
    #response = pipe(messages, max_new_tokens=5)[0]['generated_text'][1]['content']
    response = prompt
    print(response)

    return {"message": response}

@app.get("/sentiment")
def index(prompt:str):
    #messages = [
    #    {"role": "user", "content":prompt},
    #]

    response = "je n'ai pas de LLM pour vous répondre :( Achetez-vous un nouveau PC !)"
    return {"message": response}


@app.get("/docs")
def index():
    #messages = [
    #    {"role": "user", "content":prompt},
    #]
    
    import urllib
    data = urllib.urlopen(u'http://127.0.0.1:8000/docs#/')
    return data.read()
 