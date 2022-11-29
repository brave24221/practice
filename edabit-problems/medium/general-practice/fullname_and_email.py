#!/usr/bin/env python3


# Create the instance attributes fullname and email
# in the Employee class. Given a person's first and last names:

# Form the fullname by simply joining the first and last name
# together, separated by a space.
# Form the email by joining the first and last name together with a "."
# in between, and follow it with '@company.com' at the end.
# Make sure everything is in lowercase.

# Examples
# emp_1 = Employee("John", "Smith")
# emp_2 = Employee("Mary",  "Sue")
# emp_3 = Employee("Antony", "Walker")
# emp_1.fullname ➞ "John Smith"
# emp_2.email ➞ "mary.sue@company.com"
# emp_3.firstname ➞ "Antony"

# Notes
# The attributes firstname and lastname are already made for you.
# See the Resources tab for some helpful tutorials on Python classes!


# Code before:
# class Employee:
#     """Attempting to model Employee records."""
#
#     def __init__(self, firstname, lastname):
#         """Intialize the instance attritbutes."""
#         self.firstname = firstname
#         self.lastname = lastname

# Code after:
class Employee:
    """Attempting to model Employee records."""

    def __init__(self, firstname, lastname):
        """Initialize the instance attributes."""
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + " " + lastname
        self.email = firstname.lower() + "." + lastname.lower() + "@company.com"
