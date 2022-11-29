#!/usr/bin/env python3


# The packaging system is running wild!
# The candy is lying loose all over in the warehouse, the
# cereal is missing, and bread is stuffed in a bottle.
# What is going on here? The candy should be in plastic and the
# bread should be in a bag.

# The packaging machine is running the
# getContainer() function to retrieve the container of a product.
# But something is not right...

# Examples:
# get_container("Bread") ➞ "bag"
# get_container("Beer") ➞ "bottle"
# get_container("Candy") ➞ "plastic"
# get_container("Cheese") ➞ None

def get_container(product):
    matches = {
    "Bread" : "bag",
    "Milk" : "bottle",
    "Beer" : "bottle",
    "Eggs" : "carton",
    "Cerials" : "box",
    "Candy" : "plastic",
    "Cheese" : None
    }
    return matches[product
