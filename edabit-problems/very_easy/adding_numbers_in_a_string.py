# Given a string of numbers separated by a comma and space, return 
# the total sum of all the numbers.

# Examples 
# add_nums("2, 5, 1, 8, 4") ➞ 20
# add_nums("1, 2, 3, 4, 5, 6, 7") ➞ 28
# add_nums("10") ➞ 10

def adding_numbers_in_a_string(txt):
    return sum(int(i) for i in list(txt) if i not in [',', ' '])