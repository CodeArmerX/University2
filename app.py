from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')
@app.route('/calculate', methods=['POST'])
def calculate():
    return render_template('ejercicio1.html', 
    name =  request.form['name'],
    age = int(request.form['age']),
    paint = int(request.form['paint']),
    )
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')
@app.route('/login', methods=['POST'])
def login():
    return render_template('ejercicio2.html', 
    username =  request.form['username'],
    password = request.form['password'],
    )

if __name__ == '__main__':
    app.run(debug=True)