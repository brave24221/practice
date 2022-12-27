# Create a function which takes in a sentence txt and a string of
# characters chars and return the sentence but # with all the specified characters removed.

# Examples
# strip_sentence("the quick brown fox jumps over the lazy dog", "aeiou") ➞ "th qck brwn fx jmps vr th lzy dg"
# strip_sentence("the hissing snakes sinisterly slither across the rustling leaves", "s") ➞ "the hiing nake initerly lither acro the rutling leave"
# strip_sentence("gone, reduced to atoms", "go, muscat nerd") ➞ ""


def strip_sentence(txt, chars):
    return ''.join(i for i in txt if i not in chars)
