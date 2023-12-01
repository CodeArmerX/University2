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
    print(request.form)
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')
@app.route('/login', methods=['POST'])
def login():
    print(request.form)

if __name__ == '__main__':
    app.run(debug=True)