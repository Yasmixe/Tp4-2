from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1> Bienenue sur exo 6 port 8080! </h1>"


if __name__ == "__main__":
    app.run(debug=True, port=8080)
