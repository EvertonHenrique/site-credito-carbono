from flask import Flask, render_template

app = Flask(__name__)


# criar a primeira pagina do site
# route -> hashtagtreinamentos.com
# função -> o que você quer exibir naquela página

@app.route("/exemplos")
def exemplos():
    return render_template("exemplos.html")

# colocar o site no ar
if __name__ == "__main__":
    app.run()
