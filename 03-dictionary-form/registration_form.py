menuOption = 0
form = {}

while menuOption != 4:
    print("\nREGISTRATION FORM")
    print("1 - Add information to the form")
    print("2 - Retrieve information from the form")
    print("3 - Display the complete form")
    print("4 - Exit")
    menuOption = int(input("Enter your choice: "))

    if menuOption == 1:
        moreData = 'y'
        while moreData != 'n':
            personId = input("Please enter an ID (xx): ")
            key = input("Specify the field you wish to add to the form: ")
            value = input("Enter the information you wish to register in the form: ")
            if personId in form.keys():
                form[personId].update({key: value})
            else:
                form[personId] = {}
                form[personId].update({key:value})
            moreData = input("Would you like to add more information to the form? (y/n) ")

    elif menuOption == 2:
        print(f"The fields available on the form are {form.keys()} ")
        personId = input("Please specify which field you would like to display: ")

        if personId in form.keys():
            print(f"The field '{personId}' contains the data '{form[personId]}'")
        else:
            print("Invalid Option")

    elif menuOption == 3:
        print("REGISTRATION FORM")
        for field, data in form.items():
            print(f"ID: {field}")
            for key, value in data.items():
                print(f"{key}: {value}")

    elif menuOption == 4:
        print("Exiting...")
        break

    else:
        print("Invalid Option")
