from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/form2", methods=["POST"])
def form():
    return render_template("form2.html")


@app.route("/resultats2", methods=["GET", "POST"])
def index():
    val1 = request.form["vala"]
    val2 = request.form["valb"]
    val3 = request.form["valc"]
    result = int(val1) + int(val2) + int(val3)
    return render_template(
        "resultats2.html", vala=val1, valb=val2, valc=val3, resultat=result
    )


if __name__ == "__main__":
    app.run(debug=True)
