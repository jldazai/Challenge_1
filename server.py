from flask import Flask, render_template, request
import requests
import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/tables", methods=["GET","POST"])
def show_tables():
    data = db.df

    if request.method == "POST":
        lab=request.form.get("lab")
        print('####################',lab)
        print('#############################',db.consulta1(lab))

    return render_template('index.html', tables=data.to_html(classes='w3-table w3-striped w3-white'), value=db.consulta1(lab), labV=lab)

if __name__=="__main__":
    app.run(debug=True)