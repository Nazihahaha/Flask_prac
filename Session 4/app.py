from flask import Flask

app = FLask(__name__)

@app.route("/")
def home():
    return

@app.route("/signup")
def signup():
    return

@app.route("/login")
def login():
    return










if __name__ == "__main__":
    app.run(debug=True)