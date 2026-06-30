from flask import Flask, render_template, request, make_response, redirect, flash, url_for  
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user

import json

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///car.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "uewy7t7r5g34i77tr4gb3g"#notsecret

db = SQLAlchemy(app)
lm = LoginManager(app)
lm.init_app(app)
lm.login_view ="login"


class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    model_year=db.Column(db.Integer)
    price = db.Column(db.Integer)
    image = db.Column(db.String)
    descreption = db.Column(db.Text(100))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    number = db.Column(db.String(100))
    email = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=True)
    password = db.Column(db.String(100))

    cars = db.relationship("Car")


with app.app_context():
    db.create_all()

@lm.user_loader
def user_loader(id):
    return User.query.get(int(id))

@app.route("/")
def home_page():
    return render_template ("home_page.html")


@app.route("/contact")
@login_required
def contact():
    return render_template ("contact.html")

@app.route("/about")
@login_required
def about():
    return render_template ("about.html")


@app.route("/car_list")
@login_required
def car_list():
    search = request.args.get("search", "")
    if search:
        cars = Car.query.filter(Car.name.contains(search)).all()
    else:
        cars = Car.query.all()
    return render_template( "car_list.html",cars=cars,search=search)



@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        number = request.form["number"]
        email = request.form["email"]
        password = request.form["password"]

        new_user = User(
            name=name,
            number=number,
            email=email,
            password=password)
        db.session.add(new_user)
        db.session.commit( )
        flash ("registration sucessfull")
        return redirect(url_for("login"))

    return render_template ("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/")
    
    if request.method == "GET":
        return render_template ("login.html")
    
    user = User.query.filter_by(email=request.form.get("email"),
                                password=request.form.get("password"),
                                is_active=True).first()
    
    if user :
        login_user(user)
        flash ("login sucessfull")
        return redirect("/")
    
    else :
        flash ("invalid email or password")
        return redirect("/login")
    

@app.route("/activate_user/<int:id>")
@login_required
def activate_user(id):

    user = User.query.get_or_404(id)

    user.is_active = True
    db.session.commit()

    flash("User Activated")
    return redirect("/")
    
    
@app.route("/deactivate_user/<int:id>")
@login_required
def deactivate_user(id):

    user = User.query.get_or_404(id)

    user.is_active = False
    db.session.commit()

    flash("User Deactivated")
    return redirect("/")


@app.route("/logout")
@login_required
def logout():
    print("logout route called")
    logout_user()
    flash ("user logout sucessfully")
    return redirect ("/")



@app.route("/add_car", methods=["GET","POST"])
@login_required
def add_car():
    if request.method == "POST":
        name = request.form.get("name")
        brand = request.form.get("brand")
        image= request.form.get("image")
        price= request.form.get("price")
        descreption = request.form.get("descreption")
        model_year=request.form.get("model_year")

        New_car= Car(name=name,
                   brand=brand,
                   model_year=model_year,
                   image=image,
                   price=price,
                   descreption=descreption,
                   user_id=current_user.id
                   )
        db.session.add(New_car)
        db.session.commit()
        flash("car add successfully")
        return redirect(url_for("car_list"))
    return render_template ("add_car.html")


@app.route("/update/<int:id>", methods=["GET", "POST"])
@login_required
def update(id):

    car = Car.query.get(id)
    if car.user_id != current_user.id:
        flash("not update car")
        return redirect(url_for("car_list"))
    
    if request.method =="POST":
        car.name = request.form.get("name")
        car.brand = request.form.get("brand")
        car.image= request.form.get("image")
        car.price= request.form.get("price")
        car.descreption = request.form.get("descreption")
        car.model_year=request.form.get("model_year")

        db.session.commit()
        flash ("car update sucessfull")
        return redirect(url_for("car_list"))
    return render_template("update.html", car=car)


@app.route("/delete<int:id>", methods=["GET","POST"])
@login_required
def delete(id):
    car = Car.query.get(id)
    if car.user_id != current_user.id:
        flash(" not delete car ")
        return redirect(url_for("car_list"))
    if request.method == "POST":
        db.session.delete(car)
        db.session.commit()
        flash("car delete sucessfully")

    return render_template("delete.html", car=car)