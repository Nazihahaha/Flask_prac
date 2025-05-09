from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the home page</h1>"

@app.route("/welcome/steve")
def welcome_steve():
    return "<h1>Hey steve, welcome to our webpage</h1>"

@app.route("/welcome/tony")
def welcome_tony():
    return "<h1>Hey tony, welcome to our webpage</h1>"

if __name__ == "__main__":
    app.run(debug=True)
