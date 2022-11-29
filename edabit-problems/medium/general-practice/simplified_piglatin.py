#!/usr/bin/env python3


# (Simplified) Rules for converting to pig latin: 1) Move the first
# alphabet to the back of the word 2) Add the substring 'ay' to the back

# simplePigLatin('pig') →  'igpay'
# simplePigLatin('latin') →  'atinlay'
# simplePigLatin('word') → 'ordway'


def simplePigLatin(word):
    hold = word.replace(word[0], '')
    result = "{}{}{}".format(hold, word[0], 'ay')

    return result
