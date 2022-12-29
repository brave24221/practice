# You are given a list of integers having both negative and positive values, except for 
# one integer which can be negative or positive. Create a function to find out that integer.

# Examples
# lonely_integer([1, -1, 2, -2, 3]) ➞ 3
# # 3 has no matching negative appearance.

# lonely_integer([-3, 1, 2, 3, -1, -4, -2]) ➞ -4

# # -4 has no matching positive appearance.
# lonely_integer([-9, -105, -9, -9, -9, -9, 105]) ➞ -9

def lonely_integer(lst):
    return [i for i in lst if -i not in lst][0]