# Given a string of letters, how many capital letters are there?

# Examples
# capital_letters("fvLzpxmgXSDrobbgMVrc") ➞ 6
# capital_letters("JMZWCneOTFLWYwBWxyFw") ➞ 14
# capital_letters("mqeytbbjwqemcdrdsyvq") ➞ 0

def capital_letters(txt):
    return sum(1 for i in txt if i.isupper())