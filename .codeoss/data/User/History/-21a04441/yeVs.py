from flask import Flask
from 
app = Flask(__name__)
@app.route("/<username>")
def hello(username):
    return f"hello! {}"