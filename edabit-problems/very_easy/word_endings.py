# Word Endings

# Create a function that adds a string ending to each member in a list.

# Examples
# add_ending(["clever", "meek", "hurried", "nice"], "ly")
# ➞ ["cleverly", "meekly", "hurriedly", "nicely"]

# add_ending(["new", "pander", "scoop"], "er")
# ➞ ["newer", "panderer", "scooper"]

# add_ending(["bend", "sharpen", "mean"], "ing")
# ➞ ["bending", "sharpening", "meaning"]

# Notes
#     Don't forget to return the result.
#     If you get stuck on a challenge, find help in the Resources tab.
#     If you're really stuck, unlock solutions in the Solutions tab.

def add_ending(lst, ending):
    return [i + ending for i in lst]