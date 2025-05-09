from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to the home page</h1>"

@app.route("/welcome/steve")
def welcome_steve():
    return "<h1>Hey steve, welcome to our webpage</h1>"



#what if we had 100 more people, so combining the code into one single format
@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hey {name.title()}, welcome to our webpage</h1>" #-- dynamic urls






if __name__ == "__main__":
    app.run(debug=True)
