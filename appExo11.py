from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/')
def index():
  return render_template("page11.html")
  

@app.route('/data', methods=["POST"])
def doData():
  valNom      = request.form["valNom"]
  valParag    = request.form["valParag"]
  valGenre    = request.form["genre"]
  valVehicule = request.form.getlist("vehicule")
  valCars     = request.form["cars"]
  
  data={
      "nom":valNom,
      "paragraphe":valParag,
      "genre":valGenre,
      "vehicule":valVehicule,
      "cars":valCars}
  return render_template("data.html",data=data)
  
  
if __name__=='__main__':
  app.run(debug=True, port=5000)