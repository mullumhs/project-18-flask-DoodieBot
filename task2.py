from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inventory')
def inventory():
    inventory_items = ['apple', 'banana', 'cherry']
    return render_template('items.html', inventory=inventory_items)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    category = request.args.get('category', 'all')
    return f'Searching for "{query}" in category: {category}'

@app.route('/')
def page():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)