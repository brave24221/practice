# Create a function that takes a number num 
# and returns the first 10 multiples of num # with 1 added to it, separated by commas.

# Examples
# n_tables_plus_one(7) ➞ "8,15,22,29,36,43,50,57,64,71"
# n_tables_plus_one(1) ➞ "2,3,4,5,6,7,8,9,10,11"
# n_tables_plus_one(3) ➞ "4,7,10,13,16,19,22,25,28,31"


def n_tables_plus_one(num):
    return ','.join(str(num * i + 1) for i in range(1, 10 + 1))