"""
Simple Interest Calculator

Create a function that:
Takes principal, rate, time
Returns simple interest
"""


def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


si = simple_interest(1000, 5, 2)
print("Simple Interest:", si)
