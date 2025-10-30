
from main import app

# rotas
@app.route("/")
def homepage():
    return render_template("homepage.html")