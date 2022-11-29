# create a function that determines whether or not it's
# possible to split a pie fairly given these three parameters:

# total number of slices.
# number of recipients.
# how many slices each person gets.
# the function will be in this form:

# equal_slices(total slices, no. recipients, slices each)

# examples:
# equal_slices(11, 5, 2) ➞ true
# 5 people x 2 slices each = 10 slices < 11 slices

# equal_slices(11, 5, 3) ➞ false
# 5 people x 3 slices each = 15 slices > 11 slices

# equal_slices(8, 3, 2) ➞ true

# equal_slices(8, 3, 3) ➞ false

# equal_slices(24, 12, 2) ➞ true


def equal_slices(total, people, each):
    if people * each < total:
        return True
    elif total % (people * each) == 0:
        return True
    else:
        return False
