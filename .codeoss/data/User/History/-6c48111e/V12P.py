from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def default():
    return "hello world"
    
@app.route("/<user>")
def index(user):
    return f"Helllo {escape(user)}"
    

if __name__ == "__main__":
    app.run(debug=True)