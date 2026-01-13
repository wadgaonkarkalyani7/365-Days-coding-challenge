"""
Problem Statement: Check if withdrawal is possible.

Rules:
Amount ≤ balance → Transaction successful
Amount > balance → Insufficient balance
"""

balance = 5000
amount = int(input("Enter amount: "))

if amount <= balance:
    print("Transaction successful")
else:
    print("Insufficient balance")
