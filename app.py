import makeupfunctions

from flask import Flask, render_template, request

# Create an instance of Flask
app = Flask(__name__)


# Create a view function for /
@app.route('/')
def index():
    return render_template('index.html')


# Create a view function for /results
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        brand_all_lower = request.form['brand_name']
        brand = brand_all_lower.title()
        type = request.form['product_type']
        price_range = request.form['price_range']
        all_makeup = makeupfunctions.get_all_makeup()
        products = makeupfunctions.combine_all_info(all_makeup, brand, type, price_range)
        return render_template('results.html', brand=brand, type=type, products=products)
    else:
        return "Wrong HTTP method", 400
