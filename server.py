from flask import Flask
from flask import render_template
import db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello, Wordl!!'

@app.route("/tables")
def show_tables():
    data = db.df
    return render_template('index.html', tables=data.to_html(classes='w3-table w3-striped w3-white'))

if __name__=="__main__":
    app.run(debug=True)