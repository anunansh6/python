from flask import Flask,render_template
from flask import request
import json
test=Flask(__name__)

@test.route("/")
def dummy():
    return render_template("homepage.html")

@test.route("/about")
def about_func():
    return render_template("about.html")

@test.route("/login")
def blog_func():
    return render_template("login.html")

@test.route("/profile")
def login_func():
    return render_template("profile.html", b="jaipur")

@test.route("/main")
def test_args():
    return  render_template("main.html") 

@test.route("/test_form", methods=["POST", "GET"])
def test_form():
    return request.form

@test.route("/register" ,methods=["post" ,"get"])
def registration():
    return render_template("register.html")

@test.route("/a", methods=["post"])
def profile():
    
    with open ("test.json", "r") as a:
        dummy_data=json.load(a)

    new_dict={}
    new_dict["username"]=request.form["username"]
    new_dict["mail_id"]=request.form["mail_id"]
    new_dict["password"]=request.form["password"]
    new_dict["mobile"]=request.form["mobile"]
    with open ("test.json" , "w") as book :
        dummy_data.append(new_dict)

        json.dump(dummy_data,book ,indent=4)

    
    print(new_dict)
    

    return "user created sucessssfully"



# local function...
# a=2
# b=3
# print(locals())
