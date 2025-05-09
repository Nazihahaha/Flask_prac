from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the home page</h1>"


@app.route("/pass"):
def passed():
    return "Congrats you have passed"

@app.route("/fail"):
def failed():
    return "Sorry you have failed"


@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        pass
    else:
        pass




if __name__ == "__main__":
    app.run(debug=True)
