from flask import Flask
from markupsafe import escape
app = Flask(__name__)
@app.route("/<username>")
def hello(username):
    return f"hello! {escape(username)}"