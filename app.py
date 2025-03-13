from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/Welcome')
def welcome():
    return 'Welcome to Flask Web Framework'

@app.route('/products')
def showproducts():
    return 'Product Information'

@app.route('/add')
def add():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return str(a + b)

@app.route('/subtract')
def subtract():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return str(a - b)

@app.route('/multiply')
def multiply():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    return str(a * b)

@app.route('/divide')
def divide():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if b == 0:
        return 'Error: Division by zero is not allowed.'
    return str(a / b)

if __name__ == '__main__':
    print("Server running at: http://127.0.0.1:5000/")
    app.run(debug=True)