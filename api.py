from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/process")
def handle_input():
    pass