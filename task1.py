from flask import Flask,request,redirect

app = Flask(__name__)

@app.route('/search')

def search():

    query = request.args.get('q', '')

    category = request.args.get('category', 'all')

    return f'Searching for "{query}" in category: {category}'

@app.route('/hello/<name>')		
def say_hello(name):		
    return f"Hello {name}"

@app.route('/')		
def op():		
    return "in url type (/calc/num1/operation/num2) fill in with numbers <br> to add us (/+)"

@app.route('/calc/<int:num1>/<string:operation>/<int:num2>')
def calculator(num1, operation, num2): 
    if operation == "+":  
     return f'{num1} {operation} {num2} = {num1 + num2}'

if __name__ == '__main__':

    app.run(debug=True)