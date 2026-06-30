from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy
import json



data=Flask(__name__)
data.config['SQLALCHEMY_DATABASE_URI']="sqlite:///ANIL.db"
app=SQLAlchemy(data)

class User(app.Model):
    id=app.Column(app.Integer,primary_key=True)
    username=app.Column(app.String)
    email=app.Column(app.String)

class Student(app.Model):
    id=app.Column(app.Integer,primary_key=True)
    username=app.Column(app.String,sunique=True)
    email=app.Column(app.String)
    roll_number=app.Column(app.Integer)
    subject=app.Column(app.String)

    
with data.app_context():
    app.create_all()


@data.route("/list_user")
def list_user():
     
     print (data.config)
     
     with open("test.json") as book:
        dummy_data=json.load(book)
     return render_template("list_user.html", data=dummy_data)





