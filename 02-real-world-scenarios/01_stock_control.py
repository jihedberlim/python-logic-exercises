validInput = False

while not validInput:
    try:
        stockQty = int(input("Enter the quantity of items in stock for the product: "))
        if stockQty < 0:
            print("Invalid number! Stock quantity cannot be negative!")
        else:
            if stockQty < 10:
                print(f"Stock level: LOW ({stockQty} units). Consider restocking soon.")
            elif stockQty <= 50:
                print(f"Stock level: NORMAL ({stockQty} units).")
            else:
                print(f"Stock level: HIGH ({stockQty} units). Stock is well supplied.")
            validInput = True
    except:
        print("Error: please enter a valid number!")