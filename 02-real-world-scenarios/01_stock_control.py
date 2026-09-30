stockQty = int(input("Enter the quantity of items in stock for the product: "))

if stockQty < 10:
    print("low")
elif stockQty <= 50:
    print("normal")
else:
    print("high")