"""
Electricity Bill Calculator
Units consumed:
First 100 units → ₹5/unit
Next 100 units → ₹7/unit
Above 200 units → ₹10/unit

Write a program to calculate the total bill()
"""

unit = int(input("Enter units used: "))

if unit <= 100:
    bill = unit * 5

elif unit <= 200:
    bill = (100 * 5) + (unit - 100) * 7

else:
    bill = (100 * 5) + (100 * 7) + (unit - 200) * 10

print("Total Bill: ₹", bill)
