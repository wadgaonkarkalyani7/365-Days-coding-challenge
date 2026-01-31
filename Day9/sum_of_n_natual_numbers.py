# Sum of N Natural Numbers

n = int(input("Enter a number: "))

result = 0
i = 1
while i <= n:
    result = result + i
    i += 1
print(result)
