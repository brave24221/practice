# Mumbling Challenge

# Create a function that takes a string s and modifies the given string as per the below examples:

# Examples
# mumbling("MubAshIr") ➞ "M-Uu-Bbb-Aaaa-Sssss-Hhhhhh-Iiiiiii-Rrrrrrrr"
# mumbling("maTT") ➞ "M-Aa-Ttt-Tttt"
# mumbling("EdaBit") ➞ "E-Dd-Aaa-Bbbb-Iiiii-Tttttt"


def mumbling(s):
    lst = [i * v for i, v in enumerate(txt, start=1)]

    return '-'.join(i.capitalize() for i in lst)