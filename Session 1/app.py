from flask import Flask

#creating an object of our application

app = Flask(__name__)

#creating home page 
@app.route("/")
@app.route("/home") #works the same, now /home will give home page
#(creating the endpoint, whenever this endoint reached this function will be called)
def home():
    return "<h1>Welcome to the home page!</h1>"

#for path parameter, expects a user input in the url
@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Hi {name.title()}, you are welcome to this page</h1>"
                         #title makes the first letter capital

#integer path parameter
@app.route("/addition1/<int:num>")
                    #int: says to flask that it is an integer so addition takes place
def addition1(num):
    return f"<h1>Input is {num}, output in {num + 10}</h1>"


#multiple path parameter
@app.route("/addition/<int:num1>/<int:num2>")
                    #int: says flask that it is an integer so addition takes place
def addition(num1, num2):
    return f"<h1>Input is {num1, num2}, output in {num1 + num2}</h1>"


'''FUNCTION NAME CANNOT BE THE SAME'''


#creating another endpoint
@app.route("/about")
def about():
    return "<h1>Welcome to the about page!</h1>"



#start the flask application
if __name__ == "__main__":
    app.run(debug=True)

# app.run(debug=True)
#__name__ will not be main if mod1 was run, __name__ of mod1 is main then
