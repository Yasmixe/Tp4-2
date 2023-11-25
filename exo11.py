from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def form():
    return render_template("index.html")


@app.route("/data", methods=["POST"])
def index():
    valNom = request.form["valNom"]
    valparag = request.form["valparag"]
    valgenre = request.form["genre"]
    valve = request.form["vehicule"]
    valcars = request.form["cars"]
    data = {
        "nom": valNom,
        "paragraphe": valparag,
        "genre": valgenre,
        "vehicule": valve,
        "cars": valcars,
    }
    return render_template("data.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
