#!/usr/bin/env python3


# Create a function to extract the name of the subreddit from its URL.

# Examples
# sub_reddit("https://www.reddit.com/r/funny/") ➞ "funny"
# sub_reddit("https://www.reddit.com/r/relationships/") ➞ "relationships"
# sub_reddit("https://www.reddit.com/r/mildlyinteresting/") ➞ "mildlyinteresting"


def sub_reddit(link):
    hold = link.split('/')

    return hold[4]
