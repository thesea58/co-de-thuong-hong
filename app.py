from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
    render_template("static/index.html")
