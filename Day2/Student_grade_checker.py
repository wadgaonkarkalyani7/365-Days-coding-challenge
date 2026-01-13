"""
Student Grade Checker
Problem Statement: Assign grade based on marks.

Rules:
≥ 90 → A
≥ 75 → B
≥ 60 → C
≥ 40 → D
Else → Fail
"""

grade = int(input("Enter your grade: "))

if grade >= 90:
    print("A")
elif grade >= 75 and grade < 90:
    print("B")
elif grade >= 60 and grade < 75:
    print("C")
elif grade >= 40 and grade < 60:
    print("D")
else:
    print("Fail")
