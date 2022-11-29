#!/usr/bin/env python3


# Write a class called Name and create the following attributes given a first name and last name (as fname and lname):

# An attribute called fullname which returns the first and last names.
# A attribute called initials which returns the first letters of the first and last name. Put a '.' between the two letters.
# Remember to allow the attributes fname and lname to be accessed individually as well.

# Examples
# a1 = Name('john', 'SMITH')
# a1.fname ➞ 'John'
# a1.lname ➞ 'Smith'
# a1.fullname ➞ 'John Smith'
# a1.initials ➞ 'J.S'

# Notes
# Make sure only the first letter of each name is capitalised.


class Name:
    def __init__(self, fname, lname):
        """Initializing instance attributes."""
        self.fname = fname.title()
        self.lname = lname.title()
        self.fullname = fname.title() + ' ' + lname.title()
        self.initials = "{}{}{}".format(fname[0].upper(), '.', lname[0].upper())
