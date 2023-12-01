from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')
@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)