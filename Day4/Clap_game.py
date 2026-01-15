"""
Clap Game:
Print numbers from 1 to N:

If number contains 3 OR divisible by 3 → "Clap"
"""

n = int(input("Enter number: "))
for i in range(1, n + 1):
    if i % 3 == 0 or "3" in str(i):
        print("Clap")
    else:
        print(i)
