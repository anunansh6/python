from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user
from flask_login import UserMixin, login_required 
from flask import make_response, redirect 
import json
from flask import flash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///abc.db"
app.secret_key ="9938u8ruhijbfihbsdf7gfrbhbiuvu" #notsecret

lm = LoginManager(app)
lm.init_app(app)    

db = SQLAlchemy( app )

class Users( db.Model, UserMixin ):

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String, nullable = False  )
    email = db.Column( db.String, nullable = False, unique = True )
    password = db.Column( db.String, nullable = False  )
    collage = db.Column( db.String )
    photo = db.Column( db.String )
    posts = db.relationship('Post', backref='author', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    user_id = db.Column( db.Integer, db.ForeignKey('users.id'), nullable=False )

    with app.app_context():
        db.create_all()



# user_loder
@lm.user_loader
def user_fetch(id):
    return Users.query.get(int(id))

with app.app_context():
    db.create_all()


# home_page
@app.route("/")
@login_required
def home():
    return render_template("movie/base.html")


# about_page
@app.route("/about")
@login_required
def about():
    return render_template("movie/about.html")


# contact_page
@app.route("/contact")
@login_required
def contact():
    return render_template("movie/contact.html")


# profile_page
@app.route("/profile")
@login_required
def profile():
    data = Users.query.all()
    return render_template("movie/profile.html", fe_data = data)



# login_page
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return "already login user"
    if request.method == "GET":
        return render_template("movie/login.html")

    user = Users.query.filter_by(
                      email=request.form.get("email"),
                      password=request.form.get("password")).first()
    if user:
            login_user(user)
            flash('login done')
            return redirect ("/")
    else:
            flash('invalid login')
            return redirect ("/login")

@app.route("/form_args")
def form_args():
    return request.args

@app.route("/form_form", methods=["POST"])
def form_form():
    with open("test.text", "w") as file:
        file.write(str(request.form))
    return "Operation Completed Done."


# register_page
@app.route("/register", methods=["GET", 'POST'])
@login_required
def register():
    if request.method == "POST":

        a = Users(
            name = request.form.get("name"),
            email = request.form.get("email"),
            password = request.form.get("password")
        )
        image_path = f'static/{request.form.get("email")}.png'
        file = request.files["photo"]
        file.save(image_path)

        a.photo = f'{request.form.get("email")}.png'

        db.session.add(a)
        db.session.commit()
        return "User Created Successfully."
    
    return render_template("movie/register.html")


# post_page
@app.route("/create", methods=["GET", 'POST'])
def post_func():
    if request.method == "POST":
        b = Post(
        title = request.form.get("title"),
        description = request.form.get("description"),
        user_id = current_user.id
        )
        db.session.add(b)
        db.session.commit()
        flash ("post sumbit sucessfully")
    return render_template("movie/create_post.html")


# search_page
@app.route("/search")
@login_required
def search():
    if request.args:
        collage_name = request.args["collage_name"]
        data = Users.query.filter( Users.collage == collage_name ).all()
        return render_template("movie/search_collage.html", fe_data = data)

    return render_template("movie/search_collage.html")



# list_students_page
@app.route("/list_students")
@login_required
def list_students():
    data = Users.query.all()
    return render_template("movie/list_students.html", fe_data = data)


# update_student_page
@app.route("/update_student/<int:student_id>", methods=["GET", 'POST'])
@login_required
def update_student(student_id):

    data = Users.query.filter( Users.id == student_id ).first()
    if not data:
        return f"Student Not Found with id: {student_id}."

    if request.method == "POST":

        if request.form.get("name"):
            data.name = request.form.get("name")

        if request.form.get("email"):
            data.email = request.form.get("email")

        if request.form.get("password"):
            data.password = request.form.get("password")

        if request.form.get("collage"):
            data.collage = request.form.get("collage")

        db.session.add(data)
        db.session.commit()
        return "User Updated Successfully."

    return render_template("movie/update_student.html", student_id = student_id, data = data)

@app.route("/logout")
def logout():
    logout_user()
    flash ("logout done")
    return redirect("/")
    
@app.errorhandler(401)
def page_not_found(error):
    return render_template("movie/login.html")


