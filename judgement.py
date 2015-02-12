from flask import Flask, render_template, redirect, request, session
import model
# import jinja2

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'

@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/create")
def create_login():
    return render_template("create.html")

@app.route("/login", methods=["GET"])
def show_login():
    return render_template("login.html")

@app.route("/login", methods=["GET"])
def process_login():
    """TODO: Receive the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session."""

    email = request.form['email']
    password = request.form['password']
    session["email"] = email   
    return redirect("/all_users")

@app.route("/all_users")
def index():
    user_list = model.session.query(model.User).limit(5).all()
    return render_template("user_list.html", users=user_list)

if __name__ == "__main__":
    app.run(debug = True)