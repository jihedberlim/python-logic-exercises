totalSum = 0

for value in range(1, 101):
    if value % 3 == 0 or value % 5 == 0:
        totalSum += value
print(totalSum)