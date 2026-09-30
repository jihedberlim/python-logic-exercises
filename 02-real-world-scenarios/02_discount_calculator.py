addMore = 'yes'
totalPurchases = 0

while addMore != 'no':
    purchaseValue = float(input("Enter the purchase total: ").replace(",", "."))
    totalPurchases += purchaseValue
    addMore = input("Would you like to add another purchase? (yes/no) ").lower()

if totalPurchases < 100:
    print(f"TOTAL PURCHASE: ${totalPurchases:.2f}. No discount for purchases under $100.")
elif totalPurchases <= 299.99:
    discountedTotal = totalPurchases - (totalPurchases * 0.05)
    print(f"TOTAL PURCHASE: ${totalPurchases:.2f}. 5% discount applied. FINAL VALUE: ${discountedTotal:.2f}")
elif totalPurchases <= 699.99:
    discountedTotal = totalPurchases - (totalPurchases * 0.10)
    print(f"TOTAL PURCHASE: ${totalPurchases:.2f}. 10% discount applied. FINAL VALUE: ${discountedTotal:.2f}")
else:
    discountedTotal = totalPurchases - (totalPurchases * 0.15)
    print(f"TOTAL PURCHASE: ${totalPurchases:.2f}. 15% discount applied. FINAL VALUE: ${discountedTotal:.2f}")