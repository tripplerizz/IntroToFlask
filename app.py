from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/badDogs')
def badDogs():
    return "There are no bad dogs in this world."

@app.route('/goodDogs')
def goodDogs():
    return render_template("good-dogs.html")

@app.route('/myDog/<name>')
def yourDog(name):
    return "My dog's name is " + name + "."

@app.route('/myDog/Advanced/<name>')
def yourDog(name):
    return render_template("my-dog-advanced.html", name=name)

app.run()