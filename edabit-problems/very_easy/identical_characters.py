# Check if a String Contains only Identical Characters

# Write a function that returns True if all characters in a string are # identical and False otherwise.

# Examples
# is_identical("aaaaaa") ➞ True
# is_identical("aabaaa") ➞ False
# is_identical("ccccca") ➞ False
# is_identical("kk") ➞ True

# Notes
# N/A

def is_identical(s):
    return len(set(s)) == 1