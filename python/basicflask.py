from flask import Flask
app=Flask(__name__)

@app.route("/anil")
def ball():
    return "i am eating burger"

@app.route("/call")
def call():
    return "i live in india "

@app.route("/add")
def sum():
    return "a+b=0"

@app.route("/a/b")
def subtract():
    return "a-b=0"

@app.route("/")
def add():
    return "bashdbhabsfhbab"

@app.route('/user/<a>')
def show_user_profile(a):
    # show the user profile for that user
    return a









