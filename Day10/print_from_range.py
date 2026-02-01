"""
Print from a range: Display numbers from -10 to -1 using a while loop.
"""

# Easy level

# i = -10
# while i <= -1:
#     print(i)
#     i = i + 1

# intermediate level
"""
1. in function
2. range input from user
"""


def printInRange(num1, num2):
    if num1 < num2:
        i = num1
        while i <= num2:
            print(i)
            i = i + 1
    else:
        i = num1
        while i >= num2:
            print(i)
            i = i - 1


# printInRange(1, 5)
# printInRange(-1, -5)
# printInRange(5, 1)
printInRange(-5, -1)
