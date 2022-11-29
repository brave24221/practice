# Create a function that returns the number of hashes and pluses in a string.

# hash_plus_count("###+") ➞ [3, 1]
# hash_plus_count("##+++#") ➞ [3, 3]
# hash_plus_count("#+++#+#++#") ➞ [4, 6]
# hash_plus_count("") ➞ [0, 0]


def hash_plus_count(txt):
    hashes = "#"
    pluses = "+"
    empty = [0, 0]
    if txt == "":
        return empty
    else:
        return [txt.count(hashes), txt.count(pluses)]
