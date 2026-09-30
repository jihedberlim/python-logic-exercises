orderList = [150, 45, 300, 90, 500]
orderSum = 0

for value in orderList:
    if value > 100:
        orderSum += value
print(orderSum)