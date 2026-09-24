ageUser = int(input("Enter your age: "))

if ageUser >= 60:
    print("Elderly")
elif ageUser >= 18:
    print("Adult")
elif ageUser >= 13:
    print("Adolescent")
else:
    print("Child")
