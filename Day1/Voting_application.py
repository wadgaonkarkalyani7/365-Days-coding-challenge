"""
Problem Statement: Create a simple voting application that checks whether a person is eligible to vote.
Conditions:
    The user enters their age
    If the age is 18 or above, display:
    "You are eligible to vote"

    If the age is below 18, display:
    "You are not eligible to vote"()
"""

age = int(input("Enter your age: "))
if age < 0 or age > 100:
    print("Invalid age")
elif age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
