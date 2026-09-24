from pwinput import pwinput
nameUser = input("Please, enter your username: ")
print("Create a password that meets the following conditions: \n- At least 8 characters \n- At least one uppercase letter \n- At least one number \n- At least one special character")

hasMinLength = False
hasUpper = False
hasNumbers = False
hasSymbols = False


while not (hasMinLength and hasUpper and hasNumbers and hasSymbols):
    userPassword = input("Enter a password: ")

    #Verification variables
    hasMinLength = len(userPassword) >= 8
    hasUpper = False
    hasNumbers = False
    hasSymbols = False

    #Password character check
    for passChar in userPassword:

        if passChar.isupper():
            hasUpper = True
        if passChar.isdigit():
            hasNumbers = True
        if not passChar.isalnum():
            hasSymbols = True

    #Presentation of the criteria to the user
    if hasMinLength and hasUpper and hasNumbers and hasSymbols:
        print("Password is valid")
    else:
        print("Verify the following criteria")
        if hasMinLength:
            print("The word has at least 8 characters.")
        else:
            print("The word doesn't have at least 8 characters.")

        if hasUpper:
            print("The word contains an uppercase letter.")
        else:
            print("The word doesn't contain an uppercase letter.")

        if hasNumbers:
            print("The word contains a number.")
        else:
            print("The word doesn't contain numbers.")

        if hasSymbols:
            print("The word contains a symbol.")
        else:
            print("The word doesn't contain symbols.")