from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/experience")
def experience():
    return render_template("experience.html")


@app.route("/interet")
def interet():
    return render_template("interet.html")


if __name__ == "__main__":
    app.run(debug=True)
