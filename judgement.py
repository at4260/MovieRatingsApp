from flask import Flask, render_template, redirect, request, flash
from flask import session as flask_session
from model import session as model_session
import model
# import jinja2

app = Flask(__name__)
app.secret_key = 'thisisasecretkey'
# app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/create")
def create_acct():
    return render_template("create.html")

@app.route("/create", methods=["POST"])
def process_acct():
    """ToDo: use POST method to save data to database and then redirect to /login, flash that account was created succesfully"""
    email = request.form["email"]
    password =request.form["password"]
    age = request.form["age"]
    zipcode = request.form["zipcode"]
    my_new_acct = model.User(email=email, password=password , age=age , zipcode=zipcode)
    model_session.add(my_new_acct)
    model_session.commit()
    flash("Your account has been succesfully added. Please log in.")
    return redirect("/login")

@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def process_login():
    """TODO: Receive the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session."""

    email = request.form['email']
    password = request.form['password']

    # need to check that email and password combo matches the email/password in the User table

    user = model_session.query(model.User).filter(model.User.email == email).first()
    if user != None:
        if email == user.email and password == user.password:
            flask_session['email'] = email
            flash("Hello %s! Login successful."% (user.email))
            return redirect("/all_users")
        else:
            flash("Incorrect password! Try again.")
            return redirect("/login")
    else: 
        flash("Create an account first!")
        return redirect("/create")
   
@app.route("/all_users")
def index():
    """ToDo: create links for each user and send it as a GET request like the Ubermelon App"""
    user_list = model_session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)
    
if __name__ == "__main__":
    app.run(debug = True)