orderList = []
orderSum = 0
moreOrders = 'y'

while moreOrders != 'n':
    orderValue = float(input("Enter the order number: "))
    orderList.append(orderValue)
    moreOrders = input("Would you like to add more orders? (y/n): ").lower()

for value in orderList:
    if value > 100:
        orderSum += value
print(f"The sum of the values in the list are: {orderSum:.2f}")