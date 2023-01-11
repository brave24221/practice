# Remove the First and Last Characters

# Create a function that removes the first and last characters from a string.

# Examples
# remove_first_last("hello") ➞ "ell"
# remove_first_last("maybe") ➞ "ayb"
# remove_first_last("benefit") ➞ "enefi"
# remove_first_last("a") ➞ "a"

# Notes
# For words with two or fewer letters (including an empty string), return the string itself (see example #4).


def remove_first_last(txt):
return txt if len(txt) <= 2 else txt[1:-1]