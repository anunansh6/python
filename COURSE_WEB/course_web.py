from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = FLASK(__name__)
app.config["SQLALCHEMY_DATBASE_URI"] = "sqlite:///course.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False

db = SQLAlchemy(app)

class course(db.model):