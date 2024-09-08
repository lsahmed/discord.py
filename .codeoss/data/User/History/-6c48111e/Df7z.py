from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)
/z
@app.route("/<io>")
def index(io):
    return f"hello {escape(io)}"
if __name__ == "__main__":
    app.run(debug=True)