from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

# add more pictures and dogs to html tempmlate
@app.route('/goodDogs')
def goodDogs():
    return render_template("good-dogs.html")

# create route for 'badDogs'

#create route for 'myDog/<name>'

# add more info about dog to html template
@app.route('/myDog/Advanced/<name>')
def yourDogAdvanced(name):
    return render_template("my-dog-advanced.html", name=name)

app.run()