from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")


@app.route("/resultats", methods=["GET"])
def index():
    val1 = request.args.get("vala")
    val2 = request.args.get("valb")
    val3 = request.args.get("valc")
    result = int(val1) + int(val2) + int(val3)
    return render_template(
        "resultats.html", vala=val1, valb=val2, valc=val3, resultat=result
    )


if __name__ == "__main__":
    app.run(debug=True)
