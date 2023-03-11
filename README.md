# 310 final project

For this project, I am building an application using the Makeup API (https://makeup-api.herokuapp.com/)
and corresponding JSON file that allows users to find information on variuos makeup products based
on the provided search criterias. 

These are the following input values that I will be using for the index:
    - brand name
    - product type (i.e. foundation, blush, eyeliner, etc)
    - product category (i.e. liquid, pencil, powder, etc)
    - sorting price by either lowest to highest or highest to lowest
    - a default tag list provided by the API
    
Based on the input values, I will be returning the following information
for each returned product or list of products:
    - product name
    - product image (if there is no image, there will be a block with "image not available" message will be returned
    - brand name
    - product type and category (in the same line)
    - price (if there is no recorded data for the price, a "Price is not available" message will be returned
    - tag list
