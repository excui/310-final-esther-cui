# 310 final project

For this project, I am building an application using the Makeup API (https://makeup-api.herokuapp.com/)
and corresponding JSON file that allows users to find information on variuos makeup products based
on the provided search criterias. 

These are the following input values that I will be using for the index:
    - brand name
    - product type (i.e. foundation, blush, eyeliner, etc)
    - price range (less than $5, between $5 and $10, and above $10)
    
Based on the input values, I will be returning the following information
for each returned product or list of products:
    - product image (if there is no image, there will be a block with "image not available" message will be returned
    - product name
    - product type and category (in the same line)
    - price
    - product description
    - display vegan and cruelty free tags if the product has those tags
Note: the brand name will be displayed as a header as it is a required input value that users must choose.

I will only be focusing on a couple of drugstore brands that more well known in the US. The API contains
many more brands, but I want my user group to be the general American public who have more access
to drugstore and more affordable and accessible brands.
