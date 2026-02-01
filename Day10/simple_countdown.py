# Simple countdown: Take an integer input from the user and count down to zero, printing each value.
N = int(input("Enter countdown number: "))

i = N
while i >= 0:
    print(i)
    i = i - 1
