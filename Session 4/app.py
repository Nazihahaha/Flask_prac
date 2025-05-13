from flask import (Flask, render_template, url_for)

from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this is a secret key" #csrf token

@app.route("/")
def home():
    return render_template("home.html", title= "Home")

@app.route("/signup")
def signup():
    form = SignupForm()
    return render_template("signup.html", title="Sign Up", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title= "Login", form = form)










if __name__ == "__main__":
    app.run(debug=True)