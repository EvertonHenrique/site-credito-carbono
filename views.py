from flask import render_template

from main import app

# rotas
@app.route("/")
def homepage():
    return render_template("homepage.html")