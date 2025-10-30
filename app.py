from flask import Flask
#from calculadora import calculadora

app = Flask(__name__)


@app.route("/")
def home():
    return


if __name__ == "__main__":
    app.run(debug=True)