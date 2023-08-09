from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def mainPage():
    if request.method == "POST":
       input = request.form.get("input")
       converted = engkor(input)
       return render_template("result.html", input=input, output=converted)
    return render_template("index.html")


if __name__ == '__main__':
    app.run('0 .0.0.0', port=5000, debug=True)