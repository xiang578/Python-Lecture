from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Web"

@app.route('/bye')
def bye():
    return "See you later!"

@app.route('/home/<name>')
def home(name):
    return "<h1>" + name + " page</h1>"

@app.route('/add/<a>/<b>')
def add(a, b):
    return str(int(a) + int(b))

app.run(debug=True)
