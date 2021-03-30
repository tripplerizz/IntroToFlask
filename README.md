# Intro To Flask

### Introduction
Flask is a web framework for Python. It allows you to run Python code in a server hosted by your computer. It is famously used for developing web applications.  

### Resources Needed
- Python 3

### Setting Up

Create an environment:
- Clone this repository (if you don't have git, you can also just donwload it as a ZIP file).
- Within the project folder (the one you just cloned/downloaded), create a **venv** (virtual environment) folder.

- macOS: **python3 -m venv venv**
- Windows: **py -3 -m venv venv**

Activate the environment (Why use a virtual environment? Because we want our project to use dependencies that either don't exist on your system, or exist but are of a different version. Using a virtual environment allows to install dependencies to be used exclusively for our project):

- macOS: **. venv/bin/activate**
- Windows: **venv\Scripts\activate**

Install Flask:

- macOS: **pip install Flask** (use pip3 if that's what you have)
- Windows: **pip install Flask** (use pip3 if that's what you have)


### Workshop

This repository contains a skeleton for your Flask project. It has the appropiate directory and file structure for you to easily get started.

Take a look at the **app.py** file.
- This is the Flask application that will receive HTTP requests and return HTTP responses.
- It routes different endpoints (URLs) to different Python functions. 

On the templates folder, there are HTML files that the prior mentioned Python functions can render (using the functino **render_template()**)

Try routing different URL endpoints to different Python functions that render differnet HTML pages!
- This is a great example of using a backend (Flask) to handle your frontend (HTML)





