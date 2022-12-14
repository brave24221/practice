# Imagine you run a website that presents users with different coding challenges in
# levels Easy, Medium, and Hard, where users get points for completing challenges.
# An Easy challenge is worth 5 points, a Medium challenge is worth 10 points, and a # Hard challenge is worth 20 points.

# Create a function that takes the amount of challenges a user has
# completed for each challenge level, and calculates the user's total number of points.
# Keep in mind that a user cannot complete negative challenges, so the function
# should return the string "invalid" if any of the passed parameters are negative.

# Examples
# score_calculator(1, 2, 3) ➞ 85
# score_calculator(1, 0, 10) ➞ 205
# score_calculator(5, 2, -6) ➞ "invalid"


def score_calculator(easy, med, hard):
    return "invalid" if any( i < 0 for i in [easy, med, hard]) else sum([easy * 5, med * 10, hard * 20])
