from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")
# to access html files, default is templates


@app.route("/")
def home():
    return render_template("home.html", title="Home")
#invoking these hmtl files
#passing page name dynamically

@app.route("/about")
def about():
    return render_template("about.html", title="About")



if __name__ == "__main__":
    app.run(debug=True)