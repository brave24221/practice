# Mubashir needs your help to count uppercase letters, lowercase letters,
# numbers and special characters in a given string.

# Create a function which takes a string txt and returns a list of numbers with count of uppercase letters, lowercase letters, numbers and special characters.

# Examples
# filter_string("*$(#Mu12bas43hiR%@*!") ➞ [2, 6, 4, 8]
#  2 uppercase letters
#  6 lowercase letters
#  4 numbers
#  8 special characters
# filter_string("^^Edabit^^%$#12379") ➞ [1, 5, 5, 7]
# filter_string("**Airforce1**") ➞ [1, 7, 1, 4]


def filter_string(txt):
    upper = sum(1 for i in txt if i.isupper())
    lower = sum(1 for i in txt if i.islower())
    numbers = sum(1 for i in txt if i.isdigit())
    alphanum = sum(1 for i in txt if not i.isalnum())

    return [upper, lower, numbers, alphanum]
