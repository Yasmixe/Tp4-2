from flask import Flask, render_template, request

app = Flask(__name__)
persons = [
    {"nom": "john", "prenom": "doe", "point": 15},
    {"nom": "rayane", "prenom": "doe", "point": 8},
    {"nom": "bob leponge", "prenom": "doe", "point": 15},
]


@app.route("/personsdata")
def doPersons():
    return render_template("persons_list.html", data=persons)


if __name__ == "__main__":
    app.run(debug=True)
