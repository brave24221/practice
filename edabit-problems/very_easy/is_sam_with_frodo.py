# Is Sam with Frodo?

# Sam and Frodo need to be close. If they are side by side in the list, your function 
# should return True. If there is a name between them, return False.

# Examples
# middle_earth(["Frodo", "Sam", "Gandalf"]) ➞ True
# middle_earth(["Frodo", "Saruman", "Sam"]) ➞ False
# middle_earth(["Orc", "Sam", "Frodo", "Legolas"]) ➞ True

# Notes
#     No matter who comes first, the result must be True if Frodo and Sam are side by side.
#     There is only one Sam and one Frodo in the list.


def middle_earth(lst):
    if lst[lst.index('Sam') + 1] == 'Frodo':
        return True
    elif lst[lst.index('Sam') - 1] == 'Frodo':
        return True
    
    return False