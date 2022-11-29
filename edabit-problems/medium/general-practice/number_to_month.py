#!/usr/bin/env python3


# Create a function that takes a number (from 1 to 12) and
# returns its corresponding month name as a string.
# For example, if you're given 3 as input, your function should
# return "March", because March is the 3rd month.

# Number	Month Name
# 1	January
# 2	February
# 3	March
# 4	April
# 5	May
# 6	June
# 7	July
# 8	August
# 9	September
# 10	October
# 11	November
# 12	December

# Examples
# month_name(3) ➞ "March"
# month_name(12) ➞ "December"
# month_name(6) ➞ "June"


from calendar import month_name as mn
def month_name(num):
    return mn[num]
