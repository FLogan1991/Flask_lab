from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/<name>")
def hello_name(name):
    return "Hello " + name

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name) 
