from flask import Flask, redirect , url_for
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the home page</h1>"


@app.route("/pass")
def passed():
    return "<h1>Congrats you have passed</h1>"

@app.route("/fail")
def failed():
    return "<h1>Sorry you have failed</h1>"


@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        time.sleep(1)
        return redirect(url_for("failed")) #call the function name to go to that page
    else:
        return redirect(url_for("passed"))




if __name__ == "__main__":
    app.run(debug=True)
