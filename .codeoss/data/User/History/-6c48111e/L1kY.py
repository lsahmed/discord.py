from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)
@app.route("/<user>")
def index(user):
    return render_template("index.html", person=user)
    
if __name__ == "__main__":
    app.run(debug=True)