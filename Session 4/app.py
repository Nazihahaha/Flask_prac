from flask import (Flask, render_template, url_for)

app = FLask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title= "Home")

@app.route("/signup")
def signup():
    return render_template("signup.html", title="Sign Up")

@app.route("/login")
def login():
    return render_template("login.html", title= "Login")










if __name__ == "__main__":
    app.run(debug=True)