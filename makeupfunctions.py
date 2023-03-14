import urllib.parse, urllib.request, urllib.error, json
import pprint

# In this code, all of the functions needed to process the
# data to be then returned in the output will be recorded
# here. First, the API will be loaded into a readable dictionary
# through the provided JSON url. Then, the following functions
# and short corresponding descriptions will be listed below and
# then accessed in app.py


def get_all_makeup():
    url = 'http://makeup-api.herokuapp.com/api/v1/products.json'
    f = urllib.request.urlopen(url)
    makeup_api = f.read()
    makeup_data = json.loads(makeup_api)
    return makeup_data

# test:
# pprint.pprint(makeup_data)

# Function: all_brand_products
# this function will return a list of dictionaries taken from the
# makeup_data JSON that I have loaded in the code. If the
# user has inputted a brand name in the index, then that brand name
# will be used to filter out product specific to THAT brand. If the
# user left that section blank, then the original makeup_data (which
# I have called full_product_dict in the parameter) to be returned.
# Function automatically returns an empty list is the brand isn't
# in the data or if the user made a spelling error.
#
# Parameters:
# all_product_list = the full makeup data json (list)
# brand_name = the brand name input from the user (string)


def all_brand_products(all_product_list, brand_name=None):
    if brand_name == None:
        return all_product_list
    else:
        url = 'http://makeup-api.herokuapp.com/api/v1/products.json' + '?brand=' + brand_name
        f = urllib.request.urlopen(url)
        brand_data = f.read()
        brand_products_dict = json.loads(brand_data)
        return brand_products_dict


# test:
# colourpop_products = all_brand_products(makeup_data, brand_name="colourpop")
# pprint.pprint(colourpop_products)

# Function: product_type
# Based on the list returned from all_brand_products, this next function
# further filters products based on the user's desired product type.
# Whichever products in the brand list matches up with the product type
# will be returned in a new list. For example, if a user selects Revlon
# as their brand and lipstick as a product type, product_type()
#
# Paramters:
# product_list = the returned list from all_brand_products (list)
# type_name = the product type input from the user (string)


def product_type(product_list, type_name):
    products_match_type_list = []
    for product in product_list:
        if product['product_type'] == type_name:
            products_match_type_list.append(product)
    return products_match_type_list


# test:
# colourpop_lipsticks = product_type(colourpop_products, 'lipstick')
# pprint.pprint(colourpop_lipsticks)

# Function: under_five, between_five_ten, above_ten
# These next three functions have the same parameter and act very
# similarly. The one difference is on which price range will be
# included in the final list. All 3 functions take the list returned
# from product_type and they are the last filtering function before
# information is returned to the user. Listed are how each function
# acts based on the user's input:
# under_five = returns a list of products only under $5 USD
# between_five_ten = returns a list of products only between $5-10 USD
# above_ten = returns a list of products only above $10
#
# Parameters:
# product_type_list = a list of brand, and type specific products returned
#                     from product_type (list)


def under_five(product_type_list):
    under_five_list = []
    for product in product_type_list:
        usd_price = float(product['price']) * 0.72 + 2
        if usd_price < 5.0:
            under_five_list.append(product)
    return under_five_list


def between_five_ten(product_type_list):
    between_five_ten_list = []
    for product in product_type_list:
        usd_price = float(product['price']) * 0.72 + 2
        if usd_price >= 5.0 and usd_price < 10.0:
            between_five_ten_list.append(product)
    return between_five_ten_list


def above_ten(product_type_list):
    above_ten_list = []
    for product in product_type_list:
        usd_price = float(product['price']) * 0.72 + 2
        if usd_price > 10.0:
            above_ten_list.append(product)
    return above_ten_list


# example:
# cheap_colourpop_lipsticks = under_five(colourpop_lipsticks)
# middle_colourpop_lipsticks = between_five_ten(colourpop_lipsticks)
# expensive_colourpop_lipsticks = above_ten(colourpop_lipsticks)
# print("Cheap")
# pprint.pprint(cheap_colourpop_lipsticks)
# print("Middle Range")
# pprint.pprint(middle_colourpop_lipsticks)
# print("Expensive")
# pprint.pprint(expensive_colourpop_lipsticks)

# Function: combine_all_info
# This last function takes all of the previous functions to create the
# full filtered list based on brand, product type, and price range.
# This will return a list of dictionaries, where each dictionary contains
# the needed information for one product. This information will then be
# used to process in the resulting page.
#
# Parameters:
# product_list = the initial list of all products from get_all_makeup()
# brand = brand name returned from the form
# type = product type name returned from the form
# price range = price range value returned from the form


def combine_all_info(product_list, brand, type, price_range):
    brand_list = all_brand_products(product_list, brand)
    type_list = product_type(brand_list, type)
    if price_range == 'under_five':
        cheap_brand_type_list = under_five(type_list)
        final_product_list = cheap_brand_type_list
    elif price_range == 'between_five_ten':
        middle_brand_type_list = between_five_ten(type_list)
        final_product_list = middle_brand_type_list
    elif price_range == 'above_ten':
        expensive_brand_type_list = above_ten(type_list)
        final_product_list = expensive_brand_type_list
    filtered_final_list = []
    for product in final_product_list:
        new_dict = {}
        new_dict['image'] = product['image_link']
        new_dict['name'] = product['name']
        new_dict['type'] = product['product_type']
        new_dict['category'] = product['category']
        usd_price = round(float(product['price']) * 0.72 + 2)
        new_dict['price'] = '$' + str(usd_price)
        new_dict['description'] = product['description']
        if 'Vegan' in product['tag_list']:
            new_dict['vegan'] = 'Vegan'
        else:
            new_dict['vegan'] = 'Not Vegan'
        if 'cruelty free' in product['tag_list']:
            new_dict['cruelty_free'] = 'cruelty Free'
        else:
            new_dict['cruelty_free'] = 'not cruelty free'
        filtered_final_list.append(new_dict)
    return filtered_final_list


# test:
# pprint.pprint(combine_all_info(cheap_colourpop_lipsticks))
