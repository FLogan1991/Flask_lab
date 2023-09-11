from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__)
# We need to add the URL we will be using to fetch information from.
# Sometimes this means also sending some data like a key, but not for this one
url = "https://xkcd.com/info.0.json"
response = urllib.request.urlopen(url)
# Once we have the response we need to extract the data we want.
data = response.read()
dict = json.loads(data)

@app.route("/")
def hello():
    #only added the api to the home page to make the website look more clean
    return render_template("index.html", datum=dict)

@app.route("/<name>")
def hello_name(name):
    return "Hello " + name

@app.route("/about")
def about():
    name = request.args.get('name') if request.args.get('name') else "Hello World!" 
    return render_template("about.html", aboutName=name) 

if __name__ == "__main__":
    app.run(debug=True)