# Create a function that takes three 
# numbers as arguments and returns True # if it's a triangle and False if not.

# Examples
# is_triangle(2, 3, 4) ➞ True
# is_triangle(3, 4, 5) ➞ True
# is_triangle(4, 3, 8) ➞ False

def is_it_a_triangle(a, b, c)
    result = [
        a + b > c,
        a + c > b,
        b + c > a
    ]

    return all(i for i in result)