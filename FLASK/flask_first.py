from flask import Flask,render_template
from flask import request
import json
test=Flask(__name__)

@test.route("/")
def home_page():
    return render_template("home_page.html")

@test.route("/about")
def about_func():
    return render_template("abo_ut.html")

@test.route("/login")
def login_func():
    return render_template("log_in.html")

@test.route("/contact",  methods=["POST", "GET"])
def contact_func():
    return render_template("cont_act.html")
    return request.form





