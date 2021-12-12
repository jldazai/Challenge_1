from flask import Flask, render_template, request
import requests
import db

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route("/tables", methods=["GET", "POST"])
def show_tables():
    data = db.df
    if request.method == "POST":
        try:
            lab = request.form['lab']
        except:
            lab = None
        try:
            terr = request.form['terr']
        except:
            terr = None
        try:
            cant = request.form['cant']
        except:
            cant = None
        try:
            uso = request.form['uso']
        except:
            uso = None

        if lab != None:
            lab = request.form.get("lab")
            filtro = data['laboratorio_vacuna'] == lab
            return render_template('index.html', tables=data[filtro].to_html(classes='w3-table w3-striped w3-white'), value1=db.consulta1(lab), labV=lab)
        elif terr != None:
            terr = request.form.get("terr")
            filtro = data['nom_territorio'] == terr
            return render_template('index.html', tables=data[filtro].to_html(classes='w3-table w3-striped w3-white'), value2=db.consulta2(terr), terrV=terr)
        elif cant != None:
            cant = request.form.get("cant")
            filtro = data['cantidad'] <= int(cant)
            return render_template('index.html', tables=data[filtro].to_html(classes='w3-table w3-striped w3-white'), value3=cant)
        elif uso != None:
            uso = request.form.get("uso")
            filtro = data['uso_vacuna'].str.contains(
                uso, case=False, na=False, regex=False)
            return render_template('index.html', tables=data[filtro].to_html(classes='w3-table w3-striped w3-white'), value4=db.consulta4(uso), usoV=uso)
        else:
            return render_template('index.html', tables=data.to_html(classes='w3-table w3-striped w3-white'))


if __name__ == "__main__":
    app.run(debug=True)
